from flask import Flask, render_template, flash, request, redirect
from directions import direction_dict

app = Flask(__name__)
app.config.from_pyfile("config.py")
content = {}


@app.route("/", methods=["GET", "POST"])
def home():
    global content
    if request.method == "POST":
        address = request.form.get("address")
        kitchen = request.form.get("kitchen")
        master_bedroom = request.form.get("master_bedroom")
        bathroom = request.form.get("bathroom")
        electricity_and_generator = request.form.get("electricity_and_generator")
        water_supply = request.form.get("water_supply")
        stairs_and_lift = request.form.get("stairs_and_lift")
        garden_open_area = request.form.get("garden_open_area")
        drawing_dinning_living_room = request.form.get("drawing_dinning_living_room")
        children_bedroom = request.form.get("children_bedroom")
        main_gate = request.form.get("main_gate")
        result = calc_points(
            direction_dict.kitchen_dict.get(kitchen),
            direction_dict.master_bedroom_dict.get(master_bedroom),
            direction_dict.bathroom_dict.get(bathroom),
            direction_dict.electricity_and_generator_dict.get(
                electricity_and_generator
            ),
            direction_dict.water_supply_dict.get(water_supply),
            direction_dict.stairs_and_lift_dict.get(stairs_and_lift),
            direction_dict.garden_open_area_dict.get(garden_open_area),
            direction_dict.drawing_dinning_living_room_dict.get(
                drawing_dinning_living_room
            ),
            direction_dict.children_bedroom_dict.get(children_bedroom),
            direction_dict.main_gate_dict.get(main_gate),
        )
        total = result[0]
        percentage = result[1]
        length = result[2]

        content = {
            "Kitchen": kitchen
            + "|"
            + str(direction_dict.kitchen_dict.get(kitchen)),  # North|None
            "Master Bedroom": master_bedroom
            + "|"
            + str(direction_dict.master_bedroom_dict.get(master_bedroom)),
            "Bathroom": bathroom
            + "|"
            + str(direction_dict.bathroom_dict.get(bathroom)),
            "Electricity and Generator": electricity_and_generator
            + "|"
            + str(
                direction_dict.electricity_and_generator_dict.get(
                    electricity_and_generator
                )
            ),
            "Water Supply": water_supply
            + "|"
            + str(direction_dict.water_supply_dict.get(water_supply)),
            "Stairs and Lift": stairs_and_lift
            + "|"
            + str(direction_dict.stairs_and_lift_dict.get(stairs_and_lift)),
            "Garden Open Area": garden_open_area
            + "|"
            + str(direction_dict.garden_open_area_dict.get(garden_open_area)),
            "Drawing Living Dinning": drawing_dinning_living_room
            + "|"
            + str(
                direction_dict.drawing_dinning_living_room_dict.get(
                    drawing_dinning_living_room
                )
            ),
            "Children's Bedroom": children_bedroom
            + "|"
            + str(direction_dict.children_bedroom_dict.get(children_bedroom)),
            "Main Gate": main_gate
            + "|"
            + str(direction_dict.main_gate_dict.get(main_gate)),
        }
        return render_template(
            "result.html",
            content=content,
            total=total,
            percentage=percentage,
            length=length,
            address=address,
        )

    return render_template("index.html")


def calc_points(*args):
    arg_list = list(args)
    filtered_list = [x for x in arg_list if x is not None]
    if filtered_list.__len__().__eq__(0):
        print("Error")
        return 0, 0, 0
    return (
        sum(filtered_list),
        (sum(filtered_list) / (filtered_list.__len__() * 10)) * 100,
        filtered_list.__len__(),
    )


if __name__ == "__main__":
    app.run(debug=True, port=7000)
