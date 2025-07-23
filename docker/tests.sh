#!/bin/bash

# docker run --rm --name graph-machine-learning-box graph-machine-learning:latest

LOG_PREFIX="[ImageIntegrationTests]"

CMD="docker exec graph-machine-learning-box"

ARGS=$*

FILES=$(${CMD} find $* -maxdepth 2 -name "*.ipynb" | sort)

SUCCESS=0
FAILURE=0
SKIP=0

ERRORS=""

for _FILE in $FILES; do
    case $_FILE in

	./Chapter0[4,5,6,7,8,9]*)
	    echo "${LOG_PREFIX} Skipping file ${_FILE}"
	    let SKIP=SKIP+1
	    ;;
	*)
	    echo "${LOG_PREFIX} Testing ${_FILE}"
	    OUT=$(${CMD} jupyter nbconvert --execute --to notebook $_FILE --output /tmp/tmp.ipynb)
	    if [[ $? == "0" ]]; then
		let SUCCESS=SUCCESS+1
	    else
		let FAILURE=FAILURE+1
		ERRORS="${ERRORS}\n====== ${_FILE} ======\n ${OUT}\n================="
	    fi
	    ;;
    esac
done

rm -rf /tmp/tmp.ipynb

let TOTAL=SUCCESS+FAILURE+SKIP

echo "${LOG_PREFIX} "
echo "${LOG_PREFIX} ************************************* "
echo "${LOG_PREFIX} Summary"
echo "${LOG_PREFIX} ************************************* "
echo "${LOG_PREFIX} "
echo "${LOG_PREFIX} TOTAL: ${TOTAL}"
echo "${LOG_PREFIX} "
echo "${LOG_PREFIX} SUCCESS: ${SUCCESS}"
echo "${LOG_PREFIX} FAILURE: ${FAILURE}"
echo "${LOG_PREFIX} SKIP: ${SKIP}"
echo "${LOG_PREFIX} ************************************* "

# Provide 1 exit code if any failure has happened
if [[ "${FAILURE}" != "0" ]];
then
    exit 1
else
    exit 0
fi
