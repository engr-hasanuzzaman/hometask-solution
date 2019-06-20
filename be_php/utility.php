<?php

function is_dictionary($d){
  return false;
}

function is_dictionariable($d){
  return is_dictionary($d) or hasattr(d, "__dict__");
}

# ensure return python dict object
function get_dict($obj){
  if(is_dictionary($obj)){
    return $obj;
  } else {
    return vars(obj);
  }
}

function leveling($keys, $level){
  return false; //[[key, level] for key in keys];
}
  
# Simplte queue implementation
class Queue {
  public $queur = [];
  public function __construct($instanceProp){
      // $this->instanceProp = $instanceProp;
  }

  function enqueue($self, $item){
    self.queue.append($item);
  }

  function dequeue(){
    if(len(self.queue) < 1){
      return false;
    }
      
    return $this.queue.pop(0);
  }

  function size(){
    return len(self.queue);
  }
        
  function is_empty(){
    return len(self.queue) == 0;
  }
  
}
    

    