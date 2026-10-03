import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'mai_2026'
UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

players = [
    {"id": 1, "name": "Милана Щедрова",
     "position": "Центральный блокирующий",
     "number": 9,  "height": 176,
     "birth_year": 2007,
     "bio": "Лучший бомбардир прошлого сезона. Участник Первенства России и Чемпионта Москвы"},

    {"id": 16, "name": "Ева Шемелина",
     "position": "Либеро",
     "number": 1,  "height": 174,
     "birth_year": 2007,
     "bio": "Участник Чемпионта Москвы"},

    {"id": 11, "name": "Людмила Макарова",
     "position": "Связующий",
     "number": 20,  "height": 167,
     "birth_year": 2005,
     "bio": "Лучший игрок Высшей лиги А прошлого сезона"},

    {"id": 2, "name": "Виктория Акименко",
     "position": "Либеро",
     "number": 18,  "height": 160,
     "birth_year": 2008,
     "bio": "Участник МССИ"},

     {"id": 3, "name": "Евгения Глушкова",
     "position": "Диагональный",
     "number": 4,  "height": 187,
     "birth_year": 2007,
     "bio": "Участник МССИ"},

    {"id": 4, "name": "Полина Грешнева",
     "position": "Диагональный",
     "number": 14,  "height": 184,
     "birth_year": 2007,
     "bio": "Участник МССИ. Участник Чемпионата Москвы"},

     {"id": 5, "name": "Станислава Жердева",
     "position": "Доигровщик",
     "number": 8,  "height": 174,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},

     {"id": 6, "name": "Кира Кан",
     "position": "Доигровщик",
     "number": 6,  "height": 175,
     "birth_year": 2009,
     "bio": "Только пришедший в команду игрок"},

     {"id": 7, "name": "Полина Канаева",
     "position": "Центральный блокирующий",
     "number": 15,  "height": 179,
     "birth_year": 2005,
     "bio": "Участник МССИ"},

     {"id": 8, "name": "Мария Котова",
     "position": "Центральный блокирующий",
     "number": 3,  "height": 178,
     "birth_year": 2006,
     "bio": "Участник МССИ"},

     {"id": 9, "name": "Татьяна Лукьянова",
     "position": "Центральный блокирующий",
     "number": 10,  "height": 177,
     "birth_year": 2005,
     "bio": "Участник МССИ"},

     {"id": 10, "name": "Екатерина Макарова",
     "position": "Центральный блокирующий",
     "number": 5,  "height": 180,
     "birth_year": 2003,
     "bio": "Участник МССИ"},

     {"id": 12, "name": "Жанна Мозговая",
     "position": "Связующий",
     "number": 13,  "height": 160,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},

     {"id": 13, "name": "Дарья Поровицына",
     "position": "Либеро",
     "number": 12,  "height": 160,
     "birth_year": 2007,
     "bio": "Участник МССИ. Легионер"},

     {"id": 14, "name": "Светлана Соколова",
     "position": "Доигровщик",
     "number": 11,  "height": 187,
     "birth_year": 2009,
     "bio": "Только пришедший в команду игрок"},

     {"id": 15, "name": "Екатерина Чуркина",
     "position": "Доигровщик",
     "number": 7,  "height": 174,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},
]

gallery_photos = [
    {"file": "team1.jpg", "title": "Разминка перед игрой",        "desc": "Сезон 2025/2026" , "likes": 0},
    {"file": "team2.jpg", "title": "Победа",                      "desc": "Счёт 3:1" , "likes": 0},
    {"file": "team3.jpg", "title": "МАИ-МГСУ",                    "desc": "Счёт 23:11" , "likes": 0},
    {"file": "team4.jpg", "title": "Игра с РУДН",                 "desc": "Чемпионат Москвы" , "likes": 0},
    {"file": "team5.jpg", "title": "Игра с РУДН",                 "desc": "Лучший игрок" , "likes": 0},
    {"file": "team6.jpg", "title": "Общая фотография состава",    "desc": "Конец сезона" , "likes": 0},
    {"file": "team7.jpg", "title": "Награждение",                 "desc": "Второе место", "likes": 0},
    {"file": "team8.jpg", "title": "Тренировка",                  "desc": "Начало сезона", "likes": 0},
    {"file": "team9.jpg", "title": "МАИ-МГСУ",                    "desc": "Непередаваемые эмоции", "likes": 0},
    {"file": "team10.jpg", "title": "МАИ-ВШЭ",                    "desc": "Приветствие", "likes": 0},
    {"file": "team11.jpg", "title": "МАИ-ВШЭ",                    "desc": "Победное фото", "likes": 0},
    {"file": "team12.jpg", "title": "МАИ-МИИТ",                   "desc": "Тайм-аут", "likes": 0},
]

matches = [
    {"date": "2025-10-17", "opponent": "МИИТ", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2025-10-24", "opponent": "НИУ ВШЭ", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2026-10-29", "opponent": "НИУ МГСУ", "location": "СК МГСУ", "score": "2:3"},
    {"date": "2025-11-14", "opponent": "МГПУ", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2025-11-21", "opponent": "РХТУ", "location": "зал РХТУ", "score": "3:0"},
    {"date": "2025-11-28", "opponent": "МГАВМиБ-МВА", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2025-12-02", "opponent": "МГУСиТ", "location": "зал МГУСиТ", "score": "1:3"},
    {"date": "2025-12-12", "opponent": "РГУ им.Косыгина", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2026-02-13", "opponent": "МГТУ ГА", "location": "МАИ Черепаха", "score": "3:2"},
    {"date": "2026-02-20", "opponent": "МИИТ", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2026-02-26", "opponent": "НИУ ВШЭ", "location": "зал ВШЭ", "score": "3:2"},
    {"date": "2026-03-06", "opponent": "НИУ МГСУ", "location": "МАИ Черепаха", "score": "3:2"},
    {"date": "2026-03-20", "opponent": "РХТУ", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2026-03-27", "opponent": "МГАВМиБ-МВА", "location": "МАИ Черепаха", "score": "3:0"},
    {"date": "2026-04-03", "opponent": "МГУСиТ", "location": "МАИ Черепаха", "score": "0:3"},
    {"date": "2026-04-26", "opponent": "РГУ им.Косыгина", "location": "зал МГУДТ", "score": "3:0"},
    {"date": "2026-04-16", "opponent": "МГТУ ГА", "location": "СК МГТУ ГА", "score": "3:0"},
    {"date": "2026-04-27", "opponent": "МГПУ", "location": "Спортзал Института Естествознания и Спортивных Технологий МГПУ", "score": "3:1"},
]

@app.context_processor
def inject_photo_helper():
    def photo_url(filename):
        return url_for("static", filename="images/" + filename)
    return {"photo_url": photo_url}

@app.route("/")
def index():
    return render_template("index.html", players_count=len(players))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Здесь можно было бы отправить email, но пока просто покажем flash
        flash(f'Спасибо, {name}! Ваше сообщение получено.', 'success')
        return redirect(url_for("contacts"))

    return render_template("contacts.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html", matches=matches)

@app.route("/players")
def players_list():
    position = request.args.get("position", "").strip()
    search = request.args.get("search", "").strip()
    sort_by = request.args.get("sort", "number")

    filtered = players
    if position:
        filtered = [p for p in filtered if position.lower() in p["position"].lower()]
    if search:
        filtered = [p for p in filtered if search.lower() in p["name"].lower()]
    if sort_by == "number":
        filtered = sorted(filtered, key=lambda x: x["number"])
    elif sort_by == "height":
        filtered = sorted(filtered, key=lambda x: x["height"])
    elif sort_by == "birth_year":
        filtered = sorted(filtered, key=lambda x: x["birth_year"])
    elif sort_by == "name":
        filtered = sorted(filtered, key=lambda x: x["name"])

    return render_template("players.html", players=filtered, position=position, search=search, sort_by=sort_by)
@app.route("/player/<int:player_id>")
def player_detail(player_id):
    player = next((p for p in players if p["id"] == player_id), None)
    if player is None:
        return render_template("player_detail.html", player=None), 404
    return render_template("player_detail.html", player=player)

@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    errors = []
    form_data = {
        "name": "",
        "position": "",
        "number": "",
        "height": "",
        "birth_year": "",
    }

    if request.method == "POST":
        form_data["name"]       = request.form.get("name", "").strip()
        form_data["position"]   = request.form.get("position", "").strip()
        form_data["number"]     = request.form.get("number", "").strip()
        form_data["height"]     = request.form.get("height", "").strip()
        form_data["birth_year"] = request.form.get("birth_year", "").strip()

        if not form_data["name"]:
            errors.append("Укажите имя игрока.")
        elif len(form_data["name"]) < 2:
            errors.append("Имя должно содержать минимум 2 символа.")

        if not form_data["position"]:
            errors.append("Укажите амплуа игрока.")

        if not form_data["number"].isdigit():
            errors.append("Номер должен быть числом.")
        else:
            number = int(form_data["number"])
            if number < 1 or number > 99:
                errors.append("Номер должен быть в диапазоне от 1 до 99.")
            elif any(p["number"] == number for p in players):
                errors.append(f"Номер {number} уже занят другим игроком.")

        if not form_data["height"].isdigit():
            errors.append("Рост должен быть числом.")
        else:
            height = int(form_data["height"])
            if height < 150 or height > 200:
                errors.append("Рост должен быть от 150 до 200 см.")

        if not form_data["birth_year"].isdigit():
            errors.append("Год рождения должен быть числом.")
        else:
            year = int(form_data["birth_year"])
            if year < 2000 or year > 2010:
                errors.append("Год рождения должен быть от 2000 до 2010.")

        if not errors:
            new_id = max((p["id"] for p in players), default=0) + 1
            new_player = {
                "id": new_id,
                "name": form_data["name"],
                "position": form_data["position"],
                "number": int(form_data["number"]),
                "height": int(form_data["height"]),
                "birth_year": int(form_data["birth_year"]),
                "bio": "Новый игрок команды.",
            }
            players.append(new_player)

            flash(f'Игрок {new_player["name"]} успешно добавлен!', 'success')
            return redirect(url_for("players_list"))
    return render_template(
        "add_player.html",
        errors=errors,
        form_data=form_data,
    )

@app.route("/edit_player/<int:player_id>", methods=["GET", "POST"])
def edit_player(player_id):
    player = next((p for p in players if p["id"] == player_id), None)
    if player is None:
        return render_template("player_detail.html", player=None), 404

    errors = []
    form_data = {
        "name": player["name"],
        "position": player["position"],
        "number": player["number"],
        "height": player["height"],
        "birth_year": player["birth_year"],
    }

    if request.method == "POST":
        form_data["name"] = request.form.get("name", "").strip()
        form_data["position"] = request.form.get("position", "").strip()
        form_data["number"] = request.form.get("number", "").strip()
        form_data["height"] = request.form.get("height", "").strip()
        form_data["birth_year"] = request.form.get("birth_year", "").strip()

        if not form_data["name"]:
            errors.append("Укажите имя игрока.")
        elif len(form_data["name"]) < 2:
            errors.append("Имя должно содержать минимум 2 символа.")
        if not form_data["position"]:
            errors.append("Укажите амплуа игрока.")
        if not form_data["number"].isdigit():
            errors.append("Номер должен быть числом.")
        else:
            number = int(form_data["number"])
            if number < 1 or number > 99:
                errors.append("Номер должен быть в диапазоне от 1 до 99.")
            elif any(p["number"] == number and p["id"] != player_id for p in players):
                errors.append(f"Номер {number} уже занят другим игроком.")
        if not form_data["height"].isdigit():
            errors.append("Рост должен быть числом.")
        else:
            height = int(form_data["height"])
            if height < 150 or height > 200:
                errors.append("Рост должен быть от 150 до 200 см.")
        if not form_data["birth_year"].isdigit():
            errors.append("Год рождения должен быть числом.")
        else:
            year = int(form_data["birth_year"])
            if year < 2000 or year > 2010:
                errors.append("Год рождения должен быть от 2000 до 2010.")

        if not errors:
            player.update({
                "name": form_data["name"],
                "position": form_data["position"],
                "number": int(form_data["number"]),
                "height": int(form_data["height"]),
                "birth_year": int(form_data["birth_year"]),
            })
            return redirect(url_for("player_detail", player_id=player_id))

    return render_template("add_player.html", errors=errors, form_data=form_data, is_edit=True, player_id=player_id)

@app.route("/delete_player/<int:player_id>")
def delete_player(player_id):
    global players
    players = [p for p in players if p["id"] != player_id]
    return redirect(url_for("players_list"))

@app.route("/gallery", methods=["GET", "POST"])
def gallery():
    if request.method == "POST":
        file = request.files.get('photo')
        title = request.form.get('title', 'Без названия')
        desc = request.form.get('desc', '')
        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            gallery_photos.append({
                "file": filename,
                "title": title,
                "desc": desc,
                "likes": 0,
            })
        return redirect(url_for('gallery'))
    return render_template("gallery.html", photos=gallery_photos)

@app.route("/like_photo/<int:photo_id>")
def like_photo(photo_id):
    if 0 <= photo_id < len(gallery_photos):
        gallery_photos[photo_id]["likes"] += 1
    return redirect(url_for("gallery"))

@app.route("/result")
def result():
    name = request.args.get("name", "Неизвестный игрок")
    number = request.args.get("number", "—")
    return render_template("result.html", name=name, number=number)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
        app.run(debug=True)