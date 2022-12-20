const fs = require('fs');

if (process.argv[2] != null) {
    var path = process.argv[2]

    if (exists(path)) {
        if (isDirectory(path)) {
            console.log(path, 'jest katalogiem')
        } else if (isFile(path)) {
            fs.readFile(path, 'utf8', (err, data) => {
                console.log(path, 'jest plikiem, a jego zawartością jest:\n     ', data)
            });
        }
    } else {
        console.log('To coś nie istnieje!')
        return;
    }  
}

function exists(path) {
    try {
        return fs.existsSync(path);
    }
    catch (err) {
        return false
    }
}

function isDirectory(path) {
    return exists(path) && fs.statSync(path).isDirectory();
}

function isFile(path) {
    return exists(path) && fs.statSync(path).isFile();
}

exports.exists = exists
exports.isDirectory = isDirectory
exports.isFile = isFile
