# Code be Meng Li
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect
import uuid
app = Flask(__name__)
games = {
    "1":{
        "id": "1",
        "title": "Phasmophobia",
        "image":"https://static0.gamerantimages.com/wordpress/wp-content/uploads/wm/2024/10/phasmophobia-logo-over-ghost.jpg",
        "introduction": "Phasmophobia is a 4 player online co-op psychological horror. Paranormal activity is on the rise and it’s up to you and your team to use all the ghost-hunting equipment at your disposal in order to gather as much evidence as you can.The current build provides players with a large variety of ghost hunting equipment, each with three tiers of upgrades and many maps to choose from. There are also daily and weekly challenges offering plenty of replayability that will continue to grow during development.",
        "price": "14.99",
        "rate": "Overwhelmingly Positive",
        "supportive_system": ["Windows", "VR"],
        "same_system": ["9"]
    },
    "2":{
        "id": "2",
        "title": "Outlast",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/238320/header.jpg?t=1666817106",
        "introduction": "Hell is an experiment you can't survive in Outlast, a first-person survival horror game developed by veterans of some of the biggest game franchises in history. As investigative journalist Miles Upshur, explore Mount Massive Asylum and try to survive long enough to discover its terrible secret... if you dare.In the remote mountains of Colorado, horrors wait inside Mount Massive Asylum. A long-abandoned home for the mentally ill, recently re-opened by the “research and charity” branch of the transnational Murkoff Corporation, the asylum has been operating in strict secrecy… until now.",
        "price": "19.99",
        "rate": "Overwhelmingly Positive",
        "supportive_system": ["Windows", "MAC"],
        "same_system": ["5","6"]
    },
    "3":{
        "id": "3",
        "title": "3 Scary Games",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2460450/capsule_616x353.jpg?t=1714581731",
        "introduction": "You've been abducted and wake up in a man's basement. He tells you that he will kill you at midnight. A clock on the wall tells you that its 6pm. You have time find a way out, but this Man knows what he is doing. You'll need to learn from your mistakes, because he learns from his. Use items and unlock doors, all while avoiding the Man who adapts to your tactics.",
        "price": "11.99",
        "rate": "Positive",
        "supportive_system": ["Windows"],
        "same_system": ["4","7","8","10"]
    },
    "4":{
        "id": "4",
        "title": "Visage",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/594330/capsule_616x353.jpg?t=1607559678",
        "introduction": "The game is set inside a huge house in which terrible things have happened. You'll wander through the gloomy corridors, explore every dead room, and get lost in endless mazes, your head filling with memories of the dead families that once lived in this very home. This twisted environment, void of any life other than yours, takes you to places you couldn't even bear imagining.Explore a mysterious ever-changing house in a slow-paced, atmospheric world that combines both uncannily comforting and horrifyingly realistic environments, and enjoy a genuinely terrifying experience.",
        "price": "34.99",
        "rate": "Very Positive",
        "supportive_system": ["Windows"],
        "same_system": ["3","7","8","10"]
    },
    "5":{
        "id": "5",
        "title": "WORLD OF HORROR",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/913740/capsule_616x353.jpg?t=1730740660",
        "introduction": "The Old Gods are reawakening, clawing their way back into a world that's spiraling into madness. In hospitals, abandoned classrooms, quiet apartments, and dark forests, strange appearances and unexplainable phenomena test the sanity of residents in Shiokawa, Japan. Is it chaotic retribution, or the machinations of beings beyond our comprehension?This is WORLD OF HORROR: The end of the world is nigh, and the only solution is to confront the terror reigning over the apocalypse.",
        "price": "19.99",
        "rate": "Very Positive",
        "supportive_system": ["Windows", "MAC"],
        "same_system": ["2","6"]
    },
    "6":{
        "id": "6",
        "title": "Amnesia: The Dark Descent",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/57300/header.jpg?t=1727954563",
        "introduction": "Amnesia: The Dark Descent, a first person survival horror. A game about immersion, discovery and living through a nightmare. An experience that will chill you to the core.You stumble through the narrow corridors as the distant cry is heard.It is getting closer.",
        "price": "19.99",
        "rate": "Very Positive",
        "supportive_system": ["Windows", "MAC"],
        "same_system": ["2","5"]
    },
    "7":{
        "id": "7",
        "title": "Dead by Daylight",
        "image":"https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/381210/capsule_616x353.jpg?t=1738165502",
        "introduction": "Trapped forever in a realm of eldritch evil where even death is not an escape, four determined Survivors face a bloodthirsty Killer in a vicious game of nerve and wits. Pick a side and step into a world of tension and terror with horror gaming's best asymmetrical multiplayer.Dead by Daylight will be undergoing a substantial Quality of Life Initiative, which should address many longstanding concerns and frustrations our players have been experiencing.This Initiative will take place over the course of two phases. ",
        "price": "19.99",
        "rate": "Mostly Positive",
        "supportive_system": ["Windows"],
        "same_system": ["3","4","8","10"]
    },
    "8":{
        "id": "8",
        "title": "Content Warning",
        "image":"https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/2881650/capsule_616x353.jpg?t=1736717925",
        "introduction": "Film your friends doing scary things to become SpöökTube famous! Strongly advised to not go alone.Get famous or die trying! Content Warning is a co-op horror game where you film spooky stuff with your friends to try and go viral.",
        "price": "7.99",
        "rate": "Very Positive",
        "supportive_system": ["Windows"],
        "same_system": ["3","4","7","10"]
    },
    "9":{
        "id": "9",
        "title": "DEVOUR",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1274570/capsule_616x353.jpg?t=1730624650",
        "introduction": "DEVOUR is a co-op horror survival game for 1-4 players. Stop possessed cultists before they drag you to hell. Run. Scream. Hide. Just don't get caught.",
        "price": "9.99",
        "rate": "Very Positive",
        "supportive_system": ["Windows", "MAC","VR"],
        "same_system": ["1"]
    },
    "10":{
        "id": "10",
        "title": "Poppy Playtime",
        "image":"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1721470/capsule_616x353.jpg?t=1732118564",
        "introduction": "You must stay alive in this horror/puzzle adventure. Try to survive the vengeful toys waiting for you in the abandoned toy factory. Use your GrabPack to hack electrical circuits or nab anything from afar. Explore the mysterious facility... and don't get caught.",
        "price": "44.97",
        "rate": "Very Positive",
        "supportive_system": ["Windows"],
        "same_system": ["3","4","7","8"]
    }
    }   

@app.route('/')
@app.route('/welcome')
def welcome():
    selected_ids = ["1", "3", "5"]
    selected_games = [games[game_id] for game_id in selected_ids if game_id in games]
    
    return render_template("welcome.html", games=selected_games)

@app.route('/view/<id>')
def game_detail(id):
    game = games.get(id)
    if game:
        return render_template("game.html", game=game, games=games)
    else:
        return "Game not found", 404

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("query", "").strip().lower()
    if not query:
        return render_template("search.html", games=[], query="", result_count=0)

    matching_games = []
    for game in games.values():
        if (query in game["title"].lower() or 
            query in game["introduction"].lower() or 
            any(query in system.lower() for system in game["supportive_system"])):

            matching_games.append(game)

    return render_template("search.html", games=matching_games, query=query, result_count=len(matching_games))

@app.route('/add')
def add_item():
    return render_template("add.html")

@app.route('/save_game', methods=['POST'])
def save_game():
    data = request.get_json()

    name = data.get("name", "").strip()
    image = data.get("image", "").strip()
    introduction = data.get("introduction", "").strip()
    price = data.get("price", "").strip()
    rate = data.get("rate", "").strip()
    supportive_system = data.get("supportive_system", "").strip()
    same_system = ["3", "4", "7"]

    errors = {}

    if not name:
        errors["name"] = "Game Name cannot be empty."
    if not image:
        errors["image"] = "Image URL cannot be empty."
    elif not (image.startswith("http://") or image.startswith("https://")):
        errors["image"] = "Invalid URL format."
    if not introduction:
        errors["introduction"] = "Introduction cannot be empty."
    if not price:
        errors["price"] = "Price cannot be empty."
    elif not price.replace(".", "", 1).isdigit():
        errors["price"] = "Price must be a valid number."
    if not rate:
        errors["rate"] = "Rating cannot be empty."
    if not supportive_system:
        errors["supportive_system"] = "Supportive System cannot be empty."
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    game_id = str(uuid.uuid4())
    new_game = {
        "id": game_id,
        "title": name,
        "image": image,
        "introduction": introduction,
        "price": float(price),
        "rate": rate,
        "supportive_system": supportive_system.split(","),
        "same_system": same_system
    }
    games[game_id] = new_game

    return jsonify({"success": True, "game": new_game})

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_game(id):
    if id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[id]

    if request.method == 'POST':
        data = request.get_json()

        # 解析 JSON 数据
        game['title'] = data['title']
        game['image'] = data['image']
        game['introduction'] = data['introduction']
        game['price'] = float(data['price'])
        game['rate'] = (data['rate'])

        # 处理支持的系统：确保它是个列表
        game['supportive_system'] = data['supportive_system'] if isinstance(data['supportive_system'], list) else []

        print(f"Updated game {id}: {game}")  # Debugging
        return jsonify({"message": "Game updated successfully", "game": game}), 200

    return render_template("edit.html", game=game)

if __name__ == '__main__':
   app.run(debug = True, port=5001)
