<?php
  assert_options(ASSERT_ACTIVE, 1);
// check wheathe run test or not
  $isTest = false;
  if($argc > 1 && $argv[1] == 'test'){
    $isTest = true;
  }
  
  function add($arg_1, $arg_2)
  {
    
      return $arg_1 + $arg_2;
  }
 
  if (!debug_backtrace() && !$isTest) {
    print "sum of 2 and 3 is \n";
    print add(2,3);
    print "\n";
  }

  /**=========================
   * Test coverage section
   ============================**/

  function firstTest(){
    print("running first test\n");
    assert(1 == 7, "Two is less than one");
  }
  
  /**=========================
   * Run test code
   ============================**/
  if($isTest) {
    firstTest();
  }
