import QtQuick 2.13
import QtQuick.Controls 2.1

Rectangle {
    id:mainWindow
    width: 800
    height: 800
    color: "white"

    property int dim: 8

    GridView {
        id:boardGrid
        anchors.fill:parent
        cellWidth: 100; cellHeight: 100
        objectName:"boardGame"
        focus: true
        property bool blackTurn:true;
        
        model: [{posX:0,posY:0},{posX:0,posY:1},{posX:0,posY:2},{posX:0,posY:3},{posX:0,posY:4},{posX:0,posY:5},{posX:0,posY:6},{posX:0,posY:7},
                {posX:1,posY:0},{posX:1,posY:1},{posX:1,posY:2},{posX:1,posY:3},{posX:1,posY:4},{posX:1,posY:5},{posX:1,posY:6},{posX:1,posY:7},
                {posX:2,posY:0},{posX:2,posY:1},{posX:2,posY:2},{posX:2,posY:3},{posX:2,posY:4},{posX:2,posY:5},{posX:2,posY:6},{posX:2,posY:7},
                {posX:3,posY:0},{posX:3,posY:1},{posX:3,posY:2},{posX:3,posY:3},{posX:3,posY:4},{posX:3,posY:5},{posX:3,posY:6},{posX:3,posY:7},
                {posX:4,posY:0},{posX:4,posY:1},{posX:4,posY:2},{posX:4,posY:3},{posX:4,posY:4},{posX:4,posY:5},{posX:4,posY:6},{posX:4,posY:7},
                {posX:5,posY:0},{posX:5,posY:1},{posX:5,posY:2},{posX:5,posY:3},{posX:5,posY:4},{posX:5,posY:5},{posX:5,posY:6},{posX:5,posY:7},
                {posX:6,posY:0},{posX:6,posY:1},{posX:6,posY:2},{posX:6,posY:3},{posX:6,posY:4},{posX:6,posY:5},{posX:6,posY:6},{posX:6,posY:7},
                {posX:7,posY:0},{posX:7,posY:1},{posX:7,posY:2},{posX:7,posY:3},{posX:7,posY:4},{posX:7,posY:5},{posX:7,posY:6},{posX:7,posY:7}]

        function flipItem(index){
            currentIndex = index
            currentItem.flip()
        }

        delegate: Rectangle {
            color:"green"
            width:boardGrid.cellWidth
            height:boardGrid.cellHeight
            border.width:1
            border.color:"black" 

        
            Flipable {
                id: flipable
                width: parent.width
                height: parent.height
                
                property bool hasClicked:false;

                property var blackPiece: Rectangle {
                    width: 0.9*flipable.width
                    height: 0.9*flipable.height
                    color: "black"
                    border.color: "black"
                    border.width: 3
                    radius: width/2
                    anchors.centerIn: parent
                }

                property var whitePiece: Rectangle {
                    width: 0.9*flipable.width
                    height: 0.9*flipable.height
                    color: "white"
                    border.color: "black"
                    border.width: 3
                    radius: width/2
                    anchors.centerIn: parent
                }

                property var hintPiece: Rectangle {
                    width: 0.6*flipable.width
                    height: 0.6*flipable.height
                    color: "darkslategrey"
                    radius: width/2
                    anchors.centerIn: parent
                }

                property var blankPiece: Rectangle {
                    color: "green"
                }

                property bool flipped: false

                transform: Rotation {
                    id: rotation
                    origin.x: flipable.width/2
                    origin.y: flipable.height/2
                    axis.x: 1; axis.y: 0; axis.z: 0     // set axis.y to 1 to rotate around y-axis
                    angle: 0    // the default angle
                }

                states: State {
                    name: "back"
                    PropertyChanges { target: rotation; angle: -180 }
                    when: flipable.flipped
                }

                transitions: Transition {
                    NumberAnimation { target: rotation; property: "angle"; duration: 200 }
                }

            }
            
            function flip(){
                if (!flipable.hasClicked) {
                    flipable.hasClicked = true;
                    if (boardGrid.blackTurn){
                        flipable.front = flipable.blackPiece;
                        flipable.back = flipable.whitePiece;
                    }else{
                        flipable.front = flipable.whitePiece;
                        flipable.back = flipable.blackPiece
                    }
                } else {
                    flipable.flipped = !flipable.flipped
                }
                boardGrid.blackTurn = !boardGrid.blackTurn;
                console.log(boardGrid.blackTurn);
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    handler.tileClicked(index)
                    flip();
                }
            }
        }

        onWidthChanged: {
            let minSize = mainWindow.height<mainWindow.height?mainWindow.height:mainWindow.width;
            mainWindow.height=minSize;
            mainWindow.width=minSize;
            boardGrid.cellWidth = boardGrid.width/mainWindow.dim;
            boardGrid.cellHeight = cellWidth;            
        }
    }
    
}
