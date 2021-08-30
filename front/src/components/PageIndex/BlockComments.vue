<template>
  <div class="block_big" id="id_big_comments">
    <div class="block_inner" id="id_comments">

        <div id="id_comments_head">
          <h6>ЛЮДИ ПИШУТ:</h6>
          <div class="under_h6">комментарии к отправленным данным</div>
        </div>
        <comments/>

    </div>
  </div>
</template>

<script>
import Comments from "./Comments.vue"

export default {
  name: "BlockComments",
  components:{Comments},

}
</script>

<style scoped>
h6{
  font-size: 2.5em;
  margin-top: 20px;
  margin-bottom: 0;
  font-weight: 200;
  color: #b788f5;
}
.under_h6{
  font-weight: 200;
  font-size: 1.2em;
  margin-top: 15px;
  margin-bottom: 15px;
}
#id_comments{
  display: flex;
  flex-wrap: wrap;
}
#id_comments_head{
  flex: 1;
  padding: 50px 0;
}
#id_big_comments{
  background-color: ghostwhite;
}

@media only screen and (max-width: 420px) {
  #id_comments_head {
    text-align: center;
  }
}

</style>