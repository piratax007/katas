function fieldsFrom(input) {
    if (input[0] === '/') {
        const fields = input.split('\n', 2);
        
        if (fields[0].includes('[')) {
            return [getDelimiters(fields[0]), fields[1]];
        }
        
        return [fields[0][2], fields[1]];
    }

    return [/[\n,]/, input];
}

function getDelimiters(delimitersField) {
    const regex = /\[([^\]\[\r\n]*)\]/gm;
    let matches;
    const delimiters = [];

    while ((matches = regex.exec(delimitersField)) !== null) {
        if (matches.index === regex.lastIndex) {
            regex.lastIndex++;
        }

        matches.forEach((match, groupIndex) => {
            if (groupIndex === 1) {
                delimiters.push(match);
            }
        });
    }
    
    return delimiters;
}

function numbersToBeAdded(callback) {
    const [delimiters, rest] = callback;

    let std = delimiters;

    if (delimiters.length > 1) {
        std = delimiters[0];
        delimiters.forEach((d) => {rest.replace('d', std)});
        console.log(`########### ${rest}`);
    }

    return rest.split(std).map((character) => parseInt(character));
}

function negativesIn(numbers) {
    return numbers.filter(number => number < 0);
}

function searchForNegatives(numbers) {
    const negatives = negativesIn(numbers);
    return [negatives, negatives.length > 0];
}

function add(input) {
    if (input === "") {
        return 0;
    }

    const numbers = numbersToBeAdded(fieldsFrom(input)).filter(number => number < 1001);

    const [negatives, hasNegatives] = searchForNegatives(numbers);
    
    if (hasNegatives) {
        throw new Error(`negatives not allowed: ${negatives}`);
    }

    return numbers.reduce((a, b) => a + b);
}

export {add, getDelimiters};
