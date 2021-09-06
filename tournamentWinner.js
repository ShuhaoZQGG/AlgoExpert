/*
Sample Input:
competitions = [
  ['HTML', 'C#'],
  ['C#', 'Python'],
  ['Python', 'HTML']
]
results = [0, 0, 1]

Sample Output:
Winner: Python
Python: 6 points
C#: 3 points
HTML: 0 points
*/

const tournamentWinner = function (competitions, results){
  let answers = {};
  for (let i = 0; i < competitions.length; i++){
    answers[competitions[i][0]]= 0;
  }
  for (i = 0; i < competitions.length; i++){
    if (results[i] == 0){
      answers[competitions[i][1]] +=3;
    }
    else{
      answers[competitions[i][0]]+=3;
    }
  }
  let max = 0;
  let answer = '';
  for (const [key, value] of Object.entries(answers)){
    if (value > max){
      max = value;
      answer = key;
    }

  }
  console.log(answers);
  return answer;
}

const competitions = [
  ['HTML', 'C#'],
  ['C#', 'Python'],
  ['Python', 'HTML']
]

const results = [0, 0, 1]

console.log(tournamentWinner(competitions,results));