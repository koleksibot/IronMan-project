<template>
  <div id="app">
    <Base/>
  </div>
</template>

<script>
import Base from './Base.vue'

export default {
  name: 'App',
  components: {
    Base
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}
.Hide_Container{
  display: none;
}
.button_OutLine_Zero:focus{
  outline: 0;
}
.Input_OutLine_Zero:focus{
  outline: 0;
}
</style>
