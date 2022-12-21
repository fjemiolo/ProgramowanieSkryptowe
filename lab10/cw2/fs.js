const fs = require('fs');

if (process.argv[2] != null) {
    var path = process.argv[2]

    if (exists(path)) {
        if (isDirectory(path)) {
            console.log(path, 'jest katalogiem')
        } else if (isFile(path)) {
            const data = fs.readFileSync(path, {encoding:'utf8', flag:'r'});
            console.log(path, 'jest plikiem, a jego zawartością jest:\n     ', data)
        }
    } else {
        console.log('To coś nie istnieje!')
        return;
    }  
}

function exists(path) {
    return fs.existsSync(path);
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
