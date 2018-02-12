import folium
from read_list import read
import pandas

# make a map zoomed to see all the countries
map = folium.Map(location=[20, -3], zoom_start=2.52)

# make a feature group that will place the markers
# on the location of directed films
fg = folium.FeatureGroup(name="​Films")
places = read()
for k, v in places.items():
    str = ""
    for i in v:
        str += i + "\n"
    popup_res = folium.Popup(str, parse_html=True)
    fg.add_child(folium.Marker(location=k, popup=popup_res,
                               icon=folium.Icon()))

# make a dictionary that has country as key and rate as value
data_cancer = pandas.read_csv("cancer.csv")
country = data_cancer["country"]
rate = data_cancer["rate"]
csv_dict = {}
for k, v in zip(country, rate):
    csv_dict[k] = v

# make a feature group that will color the map depending
# on age-standardized rates of incident cases,
# both sexes, all cancers excluding non-melanoma
# skin cancer, worldwide in 2012
fg_cc = folium.FeatureGroup(name="Cancer_rate")
fg_cc.add_child(folium.GeoJson(data=open('world.json', 'r',
                                         encoding='utf-8-sig').read(),
                               style_function=lambda x: {'fillColor': 'red' if
                               (x['properties']['NAME'] in csv_dict.keys() and
                                csv_dict[x['properties']['NAME']] > 244.2)
                               else 'green' if
                               x['properties']['NAME'] in csv_dict.keys() and
                               (140 < csv_dict[x['properties']['NAME']] < 244)
                               else "blue" if (x['properties']['NAME'] in
                                csv_dict.keys() and
                                (csv_dict[x['properties']['NAME']] > 100 and
                                 csv_dict[x['properties']['NAME']] < 140))
                               else 'grey'}))

print("In addition to the markers that point on location "
      "where the films were directed," + "\n"
      "the map shows age-standardized rates of "
      "incident cases, both sexes, " + "\n"
      "all cancers excluding non-melanoma skin cancer, "
      "worldwide in 2012" + "\n"
      "(red - > 244.2, green - < 244.2 and > 140, "
      "blue < 140 and > 100, " + "\n"
      "grey - no data or not applicable)")

map.add_child(fg_cc)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Rybka_map.html")
