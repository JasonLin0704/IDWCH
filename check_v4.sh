#!/bin/bash

clear_log () {
	if [ -e $1 ]
  then
    rm $1
  fi
}

correction (){
  files=( $(ls .) )
  for file in "${files[@]}"
  do
    if [[ ${file} == *.cpp || ${file} == *.c ]]
    then
      echo compiling {${file}} ...
      echo compiling {${file}} ... >> score.txt
      if [[ ${file} == *.cpp ]]
      then
        g++ ${file}
      else
        gcc ${file}
      fi
      echo executing {${file}} ...
      echo executing {${file}} ... >> score.txt
      score=0
      for i in $(seq 1 1 5)
      do
        test_file=input${i}.txt
        cp ${test_file} input.txt
        
        # choose one:

        # (1) read testcases from a file
        # ./a.out > answer.txt

        # (2) use a file as stdin
        ./a.out < input.txt > answer.txt

        DIFF=$(diff output${i}.txt answer.txt)
        if [ "${DIFF}" == "" ]
        then
          echo {${test_file}} correct, +5 points. >> score.txt
          ((score += 5))
        else
          echo {${test_file}} wrong, no points. >> score.txt
          diff output${i}.txt answer.txt -aNy >> score.txt
          echo >> score.txt
        fi
        clear_log answer.txt
      done

      echo >> score.txt
      echo Total ${score} points. >> score.txt
      echo >> score.txt
      echo -------------------- >> score.txt
      echo >> score.txt

      clear_log a.out
      clear_log input.txt
    fi
  done
}

# main function
clear_log a.out
clear_log input.txt
clear_log answer.txt
clear_log score.txt
correction
