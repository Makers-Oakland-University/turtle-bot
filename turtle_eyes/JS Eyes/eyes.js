var canMaxX, canMaxY;
var eyes = [];
var screenDoor;

class Eye {
    constructor(xCoord, yCoord) {
        this.xCoord = xCoord;
        this.yCoord = yCoord;
        this.displayPosX = xCoord*canMaxX;
        this.displayPosY = yCoord*canMaxY;
        this.eyeSize = 500;
        this.eyeSpacing = this.eyeSize*(2/3);
    }
    display() {
        noStroke();
        smooth();
        fill(185, 100, 100);

        translate(this.xCoord-this.eyeSpacing, this.yCoord);
        rotate(radians(15));
        ellipse(0, 0, this.eyeSize, this.eyeSpacing);
        resetMatrix();
        translate(this.xCoord+this.eyeSpacing, this.yCoord);
        rotate(radians(180-15));
        ellipse(0, 0, this.eyeSize, this.eyeSpacing);
        resetMatrix();

        // translate(0, 0);
        
        noFill();
        this.maxItter = 20;
        for (var i = 0; i < this.maxItter; i++) {
            stroke(185, 100, 100-(i*5));

            translate(this.xCoord-this.eyeSpacing, this.yCoord);
            rotate(radians(15));
            ellipse(0, 0, this.eyeSize+i, this.eyeSpacing+i);
            resetMatrix();

            translate(this.xCoord+this.eyeSpacing, this.yCoord);
            rotate(radians(180-15));
            ellipse(0, 0, this.eyeSize+i, this.eyeSpacing+i);
            resetMatrix();
        }
    }
    blink(){
        
    }
}

class ScreenDoor {
    constructor(screenMaxX, screenMaxY){
        this.screenMaxX = screenMaxX;
        this.screenMaxY = screenMaxY;
    }
    display() {
        // for (var i = 0; i <= this.screenMaxX; i+=(this.screenMaxX/50)) {
        //     stroke(0, 0, 0, 40);
        //     line(i, 0, i, this.screenMaxY);
        //     stroke(0, 0, 0, 35);
        //     line(i+1, 0, i+1, this.screenMaxY);
        //     stroke(0, 0, 0, 30);
        //     line(i+2, 0, i+2, this.screenMaxY);
        //     stroke(0, 0, 0, 25);
        //     line(i+3, 0, i+3, this.screenMaxY);
        //     stroke(0, 0, 0, 20);
        //     line(i+4, 0, i+4, this.screenMaxY);
        //     stroke(0, 0, 0, 15);
        //     line(i+5, 0, i+5, this.screenMaxY);
        //     stroke(0, 0, 0, 10);
        //     line(i+6, 0, i+6, this.screenMaxY);
        //     stroke(0, 0, 0, 35);
        //     line(i-1, 0, i-1, this.screenMaxY);
        //     stroke(0, 0, 0, 30);
        //     line(i-2, 0, i-2, this.screenMaxY);
        //     stroke(0, 0, 0, 25);
        //     line(i-3, 0, i-3, this.screenMaxY);
        //     stroke(0, 0, 0, 20);
        //     line(i-4, 0, i-4, this.screenMaxY);
        //     stroke(0, 0, 0, 15);
        //     line(i-5, 0, i-5, this.screenMaxY);
        //     stroke(0, 0, 0, 10);
        //     line(i-6, 0, i-6, this.screenMaxY);
        // }

        for (var i = 0; i <= this.screenMaxY; i+=(this.screenMaxY/40)) {
            stroke(0, 0, 0, 40);
            line(0, i, this.screenMaxX, i);
            stroke(0, 0, 0, 35);
            line(0, i+1, this.screenMaxX, i+1);
            stroke(0, 0, 0, 30);
            line(0, i+2, this.screenMaxX, i+2);
            stroke(0, 0, 0, 25);
            line(0, i+3, this.screenMaxX, i+3);
            stroke(0, 0, 0, 20);
            line(0, i+4, this.screenMaxX, i+4);
            stroke(0, 0, 0, 15);
            line(0, i+5, this.screenMaxX, i+5);
            stroke(0, 0, 0, 10);
            line(0, i+6, this.screenMaxX, i+6);
            stroke(0, 0, 0, 35);
            line(0, i-1, this.screenMaxX, i-1);
            stroke(0, 0, 0, 30);
            line(0, i-2, this.screenMaxX, i-2);
            stroke(0, 0, 0, 25);
            line(0, i-3, this.screenMaxX, i-3);
            stroke(0, 0, 0, 20);
            line(0, i-4, this.screenMaxX, i-4);
            stroke(0, 0, 0, 15);
            line(0, i-5, this.screenMaxX, i-5);
            stroke(0, 0, 0, 10);
            line(0, i-6, this.screenMaxX, i-6);
        }
    }
}

// function preload() {

// }

function setup() {
    colorMode(HSB, 360, 100, 100, 100);
    canMaxX = $(window).width();
    canMaxY = $(window).height();
    var canvas = createCanvas(canMaxX+1 , canMaxY+1);
    canvas.parent('sketch-holder');
    screenDoor = new ScreenDoor(canMaxX, canMaxY);
    frameRate(144);
}

function draw() {
    background (0, 0, 0);
    stroke(0, 0, 0);
    // line(0, 0, canMaxX, 0);
    // line(canMaxX, 0, canMaxX, canMaxY);
    // line(canMaxX, canMaxY, 0, canMaxY);
    // line(0, canMaxY, 0, 0);

    if (mouseX>=0 && mouseX<canMaxX && mouseY>=0 && mouseY<canMaxY) {
        currEye = new Eye(mouseX, mouseY);
        eyes.pop();
        eyes.push(currEye);
    }

    for(var element of eyes) {
        element.display();
    }
    screenDoor.display();
}

// function mouseClicked() {
//     if (mouseX>=0 && mouseX<canMaxX && mouseY>=0 && mouseY<canMaxY) {
//         currEye = new Eye(mouseX, mouseY);
//         eyes.pop();
//         eyes.push(currEye);
//     }
// }

function keyPressed() {
    if (keyCode === LEFT_ARROW) {
        for(var element of eyes) {
            element.blink();
        }
    }
}