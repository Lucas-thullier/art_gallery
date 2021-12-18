<template>
  <nav id="navbar">
    <div>Un logo</div>
    <div class="link-wrapper">
      <router-link to="/">Go to Home</router-link>
      <router-link to="/painting/:id">Go to About</router-link>
    </div>
  </nav>
</template>

<style>
#navbar {
  display: flex;
  justify-content: space-between;
}

.link-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.link-wrapper * {
  margin: 0 0.5rem;
}
</style>

<script>
export default {
  name: 'Navbar',
}
</script>
