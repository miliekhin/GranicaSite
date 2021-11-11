<template>
  <router-view/>
</template>

<script>
export default {
  watch: {
    '$route'(to, from) {
      let t = 'КППшка - '
      document.title = t + to.meta.title || 'КППшка'
    }
  },
}
</script>

<style>
</style>
