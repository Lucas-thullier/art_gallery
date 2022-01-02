<script setup></script>

<template>
  <navbar></navbar>

  <router-view v-slot="{ Component }">
    <keep-alive :include="['PaintingList', 'CreatorList']">
      <component :is="Component" />
    </keep-alive>
  </router-view>
</template>

<style>
html,
body,
#app {
  min-height: 100vh;
  @apply lg:h-screen;
}

#app {
  display: flex;
  flex-direction: column;
  @apply bg-gray-700;
}

#app > section {
  flex: 1;
}

#app {
  @apply font-sans;
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
