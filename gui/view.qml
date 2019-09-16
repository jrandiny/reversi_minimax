import QtQuick 2.13
import QtQuick.Controls 2.1

Rectangle {
    width: 800
    height: 800
    color: "white"

    GridView {
        anchors.fill:parent
        cellWidth: 100; cellHeight: 100
        focus: true
        model: [{posX:0,posY:0},{posX:0,posY:1},{posX:0,posY:2},{posX:0,posY:3},{posX:0,posY:4},{posX:0,posY:5},{posX:0,posY:6},{posX:0,posY:7},
                {posX:1,posY:0},{posX:1,posY:1},{posX:1,posY:2},{posX:1,posY:3},{posX:1,posY:4},{posX:1,posY:5},{posX:1,posY:6},{posX:1,posY:7},
                {posX:2,posY:0},{posX:2,posY:1},{posX:2,posY:2},{posX:2,posY:3},{posX:2,posY:4},{posX:2,posY:5},{posX:2,posY:6},{posX:2,posY:7},
                {posX:3,posY:0},{posX:3,posY:1},{posX:3,posY:2},{posX:3,posY:3},{posX:3,posY:4},{posX:3,posY:5},{posX:3,posY:6},{posX:3,posY:7},
                {posX:4,posY:0},{posX:4,posY:1},{posX:4,posY:2},{posX:4,posY:3},{posX:4,posY:4},{posX:4,posY:5},{posX:4,posY:6},{posX:4,posY:7},
                {posX:5,posY:0},{posX:5,posY:1},{posX:5,posY:2},{posX:5,posY:3},{posX:5,posY:4},{posX:5,posY:5},{posX:5,posY:6},{posX:5,posY:7},
                {posX:6,posY:0},{posX:6,posY:1},{posX:6,posY:2},{posX:6,posY:3},{posX:6,posY:4},{posX:6,posY:5},{posX:6,posY:6},{posX:6,posY:7},
                {posX:7,posY:0},{posX:7,posY:1},{posX:7,posY:2},{posX:7,posY:3},{posX:7,posY:4},{posX:7,posY:5},{posX:7,posY:6},{posX:7,posY:7}]

        delegate: Flipable {
            id: flipable
            width: 100
            height: 100

            property bool flipped: false

            front: Image { 
                    source: "front.png"
                    anchors.centerIn: parent 
                    width: parent.width
                    height: parent.height
                }
            back: Image { 
                    source: "back.png"
                    anchors.centerIn: parent
                    width: parent.width
                    height: parent.height
                }

            transform: Rotation {
                id: rotation
                origin.x: flipable.width/2
                origin.y: flipable.height/2
                axis.x: 1; axis.y: 0; axis.z: 0     // set axis.y to 1 to rotate around y-axis
                angle: 0    // the default angle
            }

            states: State {
                name: "back"
                PropertyChanges { target: rotation; angle: 180 }
                when: flipable.flipped
            }

            transitions: Transition {
                NumberAnimation { target: rotation; property: "angle"; duration: 200 }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    flipable.flipped = !flipable.flipped
                    parent.GridView.view.currentIndex = index
                    console.log(index)
                }
            }
        }

    }
}
