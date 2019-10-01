import QtQuick 2.13
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.13

Rectangle {
    id:mainWindow
    width: 800
    height: 800/aspect
    color: "white"

    readonly property double aspect: 8/9

    property int dim: 8

    

    GridView {
        id:boardGrid
        width:mainWindow.width
        height:mainWindow.width
        cellWidth: 100; cellHeight: 100
        objectName:"boardGame"
        focus: true
        
        model: [{posX:0,posY:0},{posX:0,posY:1},{posX:0,posY:2},{posX:0,posY:3},{posX:0,posY:4},{posX:0,posY:5},{posX:0,posY:6},{posX:0,posY:7},
                {posX:1,posY:0},{posX:1,posY:1},{posX:1,posY:2},{posX:1,posY:3},{posX:1,posY:4},{posX:1,posY:5},{posX:1,posY:6},{posX:1,posY:7},
                {posX:2,posY:0},{posX:2,posY:1},{posX:2,posY:2},{posX:2,posY:3},{posX:2,posY:4},{posX:2,posY:5},{posX:2,posY:6},{posX:2,posY:7},
                {posX:3,posY:0},{posX:3,posY:1},{posX:3,posY:2},{posX:3,posY:3},{posX:3,posY:4},{posX:3,posY:5},{posX:3,posY:6},{posX:3,posY:7},
                {posX:4,posY:0},{posX:4,posY:1},{posX:4,posY:2},{posX:4,posY:3},{posX:4,posY:4},{posX:4,posY:5},{posX:4,posY:6},{posX:4,posY:7},
                {posX:5,posY:0},{posX:5,posY:1},{posX:5,posY:2},{posX:5,posY:3},{posX:5,posY:4},{posX:5,posY:5},{posX:5,posY:6},{posX:5,posY:7},
                {posX:6,posY:0},{posX:6,posY:1},{posX:6,posY:2},{posX:6,posY:3},{posX:6,posY:4},{posX:6,posY:5},{posX:6,posY:6},{posX:6,posY:7},
                {posX:7,posY:0},{posX:7,posY:1},{posX:7,posY:2},{posX:7,posY:3},{posX:7,posY:4},{posX:7,posY:5},{posX:7,posY:6},{posX:7,posY:7}]

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
                property bool isCurrentBlack: false;

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
            
            function interact(black){
                if (!flipable.hasClicked) {
                    flipable.hasClicked = true
                    flipable.isCurrentBlack = black
                    if (black){
                        flipable.front = flipable.blackPiece
                        flipable.back = flipable.whitePiece
                    }else{
                        flipable.front = flipable.whitePiece
                        flipable.back = flipable.blackPiece
                    }
                }else{
                    if(flipable.isCurrentBlack != black){
                        flipable.isCurrentBlack = !flipable.isCurrentBlack
                        flipable.flipped = !flipable.flipped
                    }
                }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    boardGrid.currentIndex = index
                    handler.tileClicked(index)
                }
            }
        }

        function interactCell(index, black){
            boardGrid.currentIndex = index
            boardGrid.currentItem.interact(black)
        }

        onWidthChanged: {
            boardGrid.cellWidth = boardGrid.width/mainWindow.dim;
            boardGrid.cellHeight = cellWidth;

            const delta = mainWindow.height - 100 - mainWindow.width;

            boardGrid.topMargin = delta/2;
            boardGrid.height = mainWindow.height - 100;          
        }
    }

    Row {
        id: scoreBoard
        anchors.top: boardGrid.bottom
        Rectangle {
            color: "white"
            width: mainWindow.width/2
            height: 100

            Text {
                id:whiteName
                color: "black"
                font.family: "Helvetica"
                font.pointSize: 18 
                anchors.horizontalCenter: parent.horizontalCenter                
            }
            
            Text {
                id:whiteScore
                color: "black"
                font.family: "Helvetica"
                font.pointSize: 24      
                anchors.centerIn: parent
            }

            Rectangle{
                id:whiteMark
                anchors.top: whiteScore.bottom
                color: "white"
                width: parent.width/5
                height: parent.height/10
                anchors.horizontalCenter: parent.horizontalCenter
                radius: width/2
                anchors.topMargin: width/7              
            }
        }
        Rectangle {
            color: "black"
            width: mainWindow.width/2
            height: 100

            Text {
                id:blackName
                color: "white"
                font.family: "Helvetica"
                font.pointSize: 18 
                anchors.horizontalCenter: parent.horizontalCenter                
            }
            
            Text {
                id:blackScore
                color: "white"
                font.family: "Helvetica"
                font.pointSize: 24      
                anchors.centerIn: parent
            }

            Rectangle{
                id:blackMark
                anchors.top: blackScore.bottom
                color: "black"
                width: parent.width/5
                height: parent.height/10
                anchors.horizontalCenter: parent.horizontalCenter
                radius: width/2
                anchors.topMargin: width/7              
            }
        }
    }

    function setScore(_whiteScore, _blackScore){
        whiteScore.text = "White : " + _whiteScore
        blackScore.text = "Black : " + _blackScore
    }

    function setMark(isBlackTurn){
        if(isBlackTurn){
            blackMark.color = "white"
            whiteMark.color = "white"
        }else{
            blackMark.color = "black"
            whiteMark.color = "black"
        }
    }

    function setName(white, black){
        blackName.text = `- ${black} -`;
        whiteName.text = `- ${white} -`;
    }
    
}
