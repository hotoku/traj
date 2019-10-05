from bottle import route, run, template, static_file, request, view
import folium
import io
import sqlite3





def get_map_html(lls):
    clat, clon = 0, 0
    # location, zoom_startは、本来、llsの中身に応じて調整するべきだが、適当な値を入れている
    fmap = folium.Map(location=[35.681236, 139.767125],
                      zoom_start=20)
    for lat, lon in lls:
        clat += lat
        clon += lon
        folium.Marker([lat, lon], popup="そのうち何か入れる").add_to(fmap)
    clat /= len(lls)
    clon /= len(lls)
    fmap.location=[clat, clon]
    with io.BytesIO() as bio:
        fmap.save(bio, close_file=False)
        ret = bio.getvalue()
    return ret

def get_trajectory(user_id):
    dbname = "db/db.sqlite"
    sql = f"""

select
  lattitude,
  longtitude
from
  positions
where
  user_id='{user_id}';

"""
    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        ret = cur.execute(sql)
        return ret.fetchall()



@route("/")
def home():
    return static_file("home.html", root="html")

@route("/show")
@view("template/show")
def show():
    user_id = request.query.user_id
    pos = get_trajectory(user_id)
    return get_map_html(pos)




run(host="localhost", port=8080, reloader=True)
