<template>
  <navbar></navbar>

  <router-view></router-view>
</template>

<style>
html,
body,
#app {
  height: 100vh;
  overflow: hidden;
}

#app {
  display: flex;
  flex-direction: column;
}

#app > section {
  flex: 1;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<script>
export default {
  name: 'App',
}
</script>
