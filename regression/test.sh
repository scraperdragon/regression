#!/bin/bash
# Horrifically brittle regression tests for the regression test module.

HAPPY="yay all tests pass :)"

echo "It passes the tests if the data is unchanged"
cp fixtures/working.pickle pickled_tests
WORKING_REAL=$( { nosetests test_actual.py > /dev/null; } 2>&1 )
WORKING_SAVE=$( { cat fixtures/working; })
if [ "$WORKING_REAL" == "$WORKING_SAVE" ]
then
    echo "  WORKING: pass"
else
    echo "  WORKING: fail"
    echo $WORKING_REAL
    echo $WORKING_SAVE
    HAPPY="boo... :("
fi

echo "It fails the tests if the data is changed"
cp fixtures/sector_0.pickle pickled_tests
SECTOR0_REAL=$( { nosetests test_actual.py > /dev/null; } 2>&1 )
SECTOR0_SAVE=$( { cat fixtures/sector_0; })
if [ "$SECTOR0_REAL" == "$SECTOR0_SAVE" ]
then
    echo "  SECTOR0: pass"
else
    echo "  SECTOR0: fail"
    echo $SECTOR0_REAL
    echo $SECTOR0_SAVE
    HAPPY="boo... :("
fi


echo "It passes if we forcibly reset the 'good' data"
python test_actual.py
LIVE_REAL=$( { nosetests test_actual.py > /dev/null; } 2>&1 )
LIVE_SAVE=$( { cat fixtures/working; })
if [ "$LIVE_REAL" == "$LIVE_SAVE" ]
then
    echo "  LIVE: pass"
else
    echo "  LIVE: fail"
    echo $LIVE_REAL
    echo $LIVE_SAVE
    HAPPY="boo... :("
fi

echo $HAPPY
