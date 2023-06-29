
function N() { return {left: W, right: NE, forward: [0, 1]}}
function NE() { return {left: N, right: E, forward: [1, 1]}}
function E() { return {left: NE, right: S, forward: [1, 0]}}
function S() { return {left: E, right: W, forward: [0, -1]}}
function W() { return {left: S, right: N, forward: [-1, 0]}}



function createRover(x,y,direction){
    return {
        x:x,
        y:y,
        direction: direction,
    };
}

function createWorld(width, height) {
    return function(rover, [dx, dy]) {
        return {
            x: rover.x + dx,
            y: rover.y + dy,
            direction: rover.direction,
        }
    }
}

function L(rover) {
    return newRoverWithDirection(rover, rover.direction().left)
}
function U(rover) {
    return newRoverWithDirection(rover, rover.direction())
}

function R(rover) {
    return newRoverWithDirection(rover, rover.direction().right)
}

function M(rover) {
    return applyDirectionChange(rover, rover.direction().forward)
}

function moveRoverOnce(instruction, rover){
    switch (instruction) {
        case "L": rover.direction().left    return createRover(rover.x, rover.y, turnToLeft(rover.direction))
        case "R": rover.direction().right return createRover(rover.x, rover.y, turnToRight(rover.direction))
        case "M": applyDirectionChange(rover, rover.direction().forward) return createRover(newXPosition(rover.x, rover.direction), newYPosition(rover.y, rover.direction), rover.direction);
    }
}

function newXPosition(currentX, direction){
    switch(direction){
        case "E": return currentX+1;
        case "W": return currentX-1;
        default: return currentX;
    }
}

function newYPosition(currentY, direction){
    switch(direction){
        case "N": return currentY+1;
        case "S": return currentY-1;
        default: return currentY;
    }
}

function turnToLeft(direction){
    return  {
        N: "W",
        W: "S",
        S: "E",
        E: "N" }
        [direction]
}

function turnToRight(direction){
    return  {
        N: "E",
        W: "N",
        S: "W",
        E: "S" }
        [direction]
}

export {createRover, moveRoverOnce};
