<template>
  <footer class="block_big" id="id_big_foot">
    <div class="block_inner" id="id_foot">
          &copy;2021 КППшка
    </div>
  </footer>
</template>

<script>
export default {
  name: "BlockFooter"
}
</script>

<style scoped>
#id_big_foot{
  color: #ba6d35;
  background-color: #202020;
  line-height: 50px;
}
@media only screen and (max-width: 420px) {
  #id_foot {
    text-align: center;
  }
}

</style>