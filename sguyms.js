const { exec } = require('child_process');
const fs = require('fs');

let variables = {}

class Variable{
    constructor(name, value) {
        this.name = name;
        this.value = value;
    }

    hold(){
        variables[this.name] = this.value;
    }
}

function get(variable) {
    return variables[variable]
}

function call_py(script_id, func_name, args = ''){
    fs.writeFile('./running/call.py', `from running${script_id} import *\n${func_name}(${args})`, 'utf8', (writeErr) => {
        if (writeErr) {
            console.error(writeErr);
            return;
        }

        exec('python ./running/call.py', (execError, stdout, stderr) => {
            if (execError) {
                console.error(execError);
                return;
            }
            if (stderr) {
                console.error(stderr);
                return;
            }
            console.log(stdout);
        });
    });
}

function call_node(script_id, func_name, args = ''){
    fs.writeFile('./running/call.js', `let sgms = require("./running${script_id}.js");\nsgms.${func_name}(${args});`, 'utf8', (writeErr) => {
        if (writeErr) {
            console.error(writeErr);
            return;
        }

        exec('node ./running/call.js', (execError, stdout, stderr) => {
            if (execError) {
                console.error(execError);
                return;
            }
            if (stderr) {
                console.error(stderr);
                return;
            }
            console.log(stdout);
        });
    });
}

function load(){
    try {
      const data = fs.readFileSync('./running/variables.json', 'utf8');
      try {
          const variables = JSON.parse(data);
      } catch (error) {
          console.error(error.message);
      }
    } catch (err) {
      console.error(err);
    }
}

function save(){
    try {
      fs.writeFileSync('./running/variables.json', JSON.stringify(variables), 'utf8');
    } catch (err) {
      console.error(err);
    }
}

module.exports = {
    call_py,
    load,
    save,
    get,
    call_node,
    Variable
}