var data = [
    {
        Name: 'Mark',
        Age: 43,
    },
    {
        Name: 'Bob',
        Age: 33,
    },
    {
        Name: 'Julia',
        Age: 51,
    },
    {
        Name: 'Sam',
        Age: 31,
    },
]
var ch = 'J';
for (var i = 0; i < data.length; i++) {
    if (data[i]['Name'][0] === 'S' || data[i]['Name'][0] === 'J' || data[i]['Age'] < 35) {
        console.log(data[i]['Name'] + " " + i)
    }
}