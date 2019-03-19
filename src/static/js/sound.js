function playSound(groupIndex, soundIndex) {
    if (conn === null) {
        console.log("No connection established!");
        return;
    }
    const toSend = {
        "action": "playSound",
        "groupIndex": groupIndex,
        "soundIndex": soundIndex,
    };
    conn.send(JSON.stringify(toSend));
}

function setSoundVolume() {
    const volume = $("#sound-volume").val();
    if (conn === null) {
        console.log("No connection established!");
        return;
    }
    const toSend = {
        "action": "setSoundVolume",
        "volume": volume,
    };
    conn.send(JSON.stringify(toSend));
}