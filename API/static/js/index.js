class Passenger {
    constructor(PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, Survived) {
        this.PassengerId = PassengerId;
        this.Pclass = Pclass;
        this.Name = Name;
        this.Sex = Sex;
        this.Age = Age;
        this.SibSp = SibSp;
        this.Parch = Parch;
        this.Ticket = Ticket;
        this.Fare = Fare;
        this.Cabin = Cabin;
        this.Embarked = Embarked;
        this.Survived = Survived;
    }
    static parseObject(passenger) {
        if (passenger.length > 1) {
            tmpPassenger =  new Passenger(0, 1, passenger[1], "male", 42, 42, 42, "42", 666, "C42", "C", passenger[0])
            return tmpPassenger
        }
    }
    static parseArray(array) {
        array.forEach(element => {
            element = this.parseObject(element)
        });
        return array
    }
};
let predictions = []

function sendData() {
    let data = null;
    let input = document.getElementById("filePassengers");
    if (input.files[0]) {
        data = new FormData();
        data.append('file', input.files[0]);
    } else if (document.getElementById("inputAge").value) {
        data = [];
        tmpPassenger = new Passenger(parseInt(document.getElementById("inputPassengerId").value),
            parseInt(document.getElementById("inputPClass").value),
            document.getElementById("inputName").value,
            document.getElementById("inputSex").value,
            parseFloat(document.getElementById("inputAge").value),
            parseInt(document.getElementById("inputSibSp").value),
            parseInt(document.getElementById("inputParch").value),
            330911,
            parseFloat(document.getElementById("inputFare").value),
            "",
            document.getElementById("inputEmbarked").value,
            0)
        data.push(tmpPassenger);
        data = JSON.stringify(data)
        fetch("https://titanique.herokuapp.com/prediction", {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "post",
                body: data
            })
            .then(response =>
                response.json())
            .then(data => {
                console.log(data);
                predictions = JSON.parse(data.predictions);
                generateTable();
            });
            return;
    } else {
        alert("Veuillez charger un fichier / remplir les champs");
        return;
    }
    fetch("https://titanique.herokuapp.com/prediction", {
            method: "post",
            body: data
        })
        .then(response =>
            response.json())
        .then(data => {
            console.log(data);
            predictions = JSON.parse(data.predictions);
            generateTable();
        });
}

function generateTable() {
    table = document.getElementById("tbodyResults");
    table.innerHTML=""
    console.log("Predictions");
    console.log(predictions);
    for (let index = 0; index < predictions.length; index++) {
        var row = table.insertRow(index);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        if(predictions[index][0]){
            cell1.innerHTML = "🤕";
        }
        else
        {
            cell1.innerHTML = "💀";
        }
        cell2.innerHTML = predictions[index][1];
    }
    showTable(true);
}

function showTable(isShowed) {
    table = document.getElementById("tableResults")
    if (isShowed) {
        table.style.display = "table";
    } else {
        table.style.display = "none";
    }
}