# Questions section
**Write a video player application with ‘Play’, ‘Forward’ , ‘Rewind’ functionalities. Please
write pseudocode for this program and explain the design pattern you will use to develop
these three functionalities.**

# Answer section
## Selection of design pattern
Since we are going to build a video player application which has three states ‘Play’, ‘Forward’ , ‘Rewind’, I am going to use state design pattern (SDP) that focuses on the different states in an application, transitions between states, and the different behaviors within a state. Each state object implements the interface in a way appropriate for the state. Because of this structure, no conditional statements are required to branch differentially depending on the current state. Rather than writing complex conditional statements, the individual state objects define how the methods are to behave for that state.

For example, with a three state video player the following pseudo code could direct the state behavior to start playing the video depending on the state machine's current state:

```code
function play(){
   if(state == Play) {
      print("You're already playing.");
   }
   else if (state == Forward){
      print("stop forward and start play stat)
   } else if (state == Rewind){
     print("stop Rewind and start play stat)
   }
}
```code
 
 The above branch condition will be more compltex if we need to add more state to our player.


## Pseudocode
interface State {
  function play()
  function rewind()
  function forward()
}

// concrete state implementation
class PlayState implements State {
  // implementation of different methods for this state
  function play(){
    print("you are already on play mode")
  }

  function rewind(){
    print("stop play and start rewind")
  }

  function forward(){
    print("stop play and start forward")
  }
}

class ForwardState implements State {
  // implementation of different methods for this state
  function play(){
    print("stop forward and start play")
  }

  function rewind(){
    print("stop rewind and start forward")
  }

  function forward(){
    print("you are already on forward mode")
  }
}

class RewindState implements State {
  // implementation of different methods for this state
 function play(){
    print("stop rewind and start play")
  }

  function rewind(){
    print("you are already on rewind mode")
  }

  function forward(){
    print("stop rewind and start forward")
  }
}

// implementation of VideoPlayer Class
Class VideoPlayer {
  private state State
  private playState PlayState
  private rewindState RewindState
  private forwardState ForwardState

  constructor(){
    this.playState = new PlayState()
    this.rewindState = new PlayState()
    this.forwardState = new PlayState()
    this.state = this.playstate
  }

  State function getState() {
    return this.state
  }
  
  State function setState(state State) {
    this.state = state
  }

  void function startPlay() {
    this.state.play()
  }

  void function startForward() {
    this.state.forward()
  }

  void function startRewind() {
    this.state.rewind()
  }
}