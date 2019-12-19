# Download and create the dataset from URLs
# s1 + s2
import requests

def fn_read(path): # Függvény, ami beolvassa az adott txt fájlból a linkeket
    f = open(path, 'r', errors='ignore')  # file megnyitása #errors = ignore nélkül a második hívásnál UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1447: character maps to <undefined>-t dobott ?!
    list = f.readlines() # Soronként beolvassuk az url-eket egy stringeket tartalmazó listába
    f.close()

    return list

def fn_download(list, type, path):  # Fv, ami letölti a paraméterként megkapott listában lévő linkekről a képeket, olyan típusból amit a name-ben megadtunk és arra a helyre menti amit megadtunk
    error= 0
    for i in range(len(list)):
        #if ("flickr" in list[i]): # A tapasztalatok szerint a flickr.com-ról letöltött képek nagyobb százalékban bizonyulnak használhatónak
        try:
            url = list[i]  # Az adott url amiről letöltünk a listánk i-edik eleme lesz
            r = requests.get(url)  # Megadjuk ezt az url-t a letöltéshez
            fname = type + "{}"
            fpath = path + "\\" + fname.format(i) + ".jpg"
            open(fpath, 'wb').write(r.content)  # Új fájlt hozunk létre, amibe lementjük a letöltött képet
            print(i)
        except IOError:
            error = error + 1
            # Stop in case you reach 100 errors downloading images
            if error > 100:
                break
            else:
                print("File does not exist")
    print('Download is done')


# Person képek 1241 db letöltve, 1146 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\person\person_urls.txt"
# fn_download(fn_read(path), "personb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\person")

# Bird képek 839 db letöltve 1177 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bird\bird_urls.txt"
# fn_download(fn_read(path), "birda" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bird")

# Cat képek 1031 db letöltve 1023 db használható kép # domestic cat-ből

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\cat\cat_urls.txt"
# fn_download(fn_read(path), "catb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\cat")

# Cow képek 1185 db letöltve 1000 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\cow\cow_urls.txt"
# fn_download(fn_read(path), "cowa" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\cow")

# Dog képek 1020 db letöltve 1000 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\dog\dog_urls.txt"
# fn_download(fn_read(path), "dogc" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\dog")

# Horse képek 1320 db letöltve 1089 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\horse\horse_urls.txt"
# fn_download(fn_read(path), "horsee" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\horse")

# Sheep képek 1026 db letöltve 1009 db használható rohadt bárány

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\sheep\sheep_urls.txt"
# fn_download(fn_read(path), "sheepzzzzz" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\sheep")

# Airplane képek 914 db letöltve 1051 db használható kép aircraft

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\airplane\airplane_urls.txt"
# fn_download(fn_read(path), "airplanez" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\airplane")

# Bicycle képek 1270 db letöltve 788 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bicycle\bicycle_urls.txt"
# fn_download(fn_read(path), "bicycles" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bicycle")

# Boat képek 1034 db letöltve 1002 db használható kép (innentől nem a legjobb az annotáció)

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\boat\boat_urls.txt"
# fn_download(fn_read(path), "boatc" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\boat")

# Bus képek 1334 db letöltve 1116 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bus\bus_urls.txt"
# fn_download(fn_read(path), "busb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bus")

# Car képek 1209 db letöltve 1051 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\car\car_urls.txt"
# fn_download(fn_read(path), "carb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\car")

# Motorbike képek 1199 db letöltve 1000 db használható

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\motorbike\motorbike_urls.txt"
#fn_download(fn_read(path), "motorbikeb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\motorbike")

# Train képek 1282 db letöltve 1044 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\train\train_urls.txt"
# fn_download(fn_read(path), "trainb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\train")

# Bottle képek 1177 db letöltve 1002 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bottle\bottle_urls.txt"
# fn_download(fn_read(path), "bottleb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\bottle")

# Chair képek 1422 db letöltve 1000 db használható kép
# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\chair\chair_urls.txt"
# fn_download(fn_read(path), "chair" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\chair")

# Table képek (n04379243) (n04379964) (n03063968) (n03090000) (n03201208) (n03231368) 1002 db

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\table\table_urls.txt"
# fn_download(fn_read(path), "tablezs" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\table")

# Plant képek 1261 db letöltve 1008 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\plant\plant_urls.txt"
# fn_download(fn_read(path), "plantc" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\plant")

# Sofa képek 671 db letöltve 1002 db

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\sofa\sofa_urls.txt"
# fn_download(fn_read(path), "sofac" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\sofa")

# TV képek 763 db kép letöltve (tv mappa) 1000 db használható kép

# path = r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\tv\tv_urls.txt"
# fn_download(fn_read(path), "tvb" , r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\tv")