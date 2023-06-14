<template>
  <div class="block_card">
    <div
        class="card_head"
        :class="onStart"
    >
      <div class="id_add_data_block">
        <div class="id_add_data_head">
          Опишите суть и причину проблемы. Предложите решение.
        </div>
        <kp-button text="НАПИСАТЬ ЖАЛОБУ" @click="startAdder"/>
      </div>
    </div>
  </div>
</template>

<script>
import KpButton from "../Info/KpButton.vue";

export default{
  name: "InfoAdderComplaint",
  components: {
    KpButton,
  },
  props: [
    'is_inited',
    'kpps',
  ],
  data() {
    return{
      onStart: 'onStart',
    }
  },
  methods: {
    startAdder() {
      if(!this.is_inited){
        this.emitter.emit('fetch_error', 'Сайт ещё не готов к работе.')
        return;
      }

    },
  },
}
</script>

<style scoped>
  .info_card{
    padding: 15px;
    border: #404040 solid 1px;
    width: 380px;
    box-sizing: border-box;
    background-color: rgba(31, 56, 69, .7);
    height: 383px;
  }
  .id_info_wrp{
    display: flex;
    max-width: 350px;
    flex-direction: column;
    margin: auto;
    height: 250px;
  }
  .id_add_data_head{
    font-size: .8em;
    text-align: center;
    color: #ddd;
  }
  .onStart{
    justify-content: space-around;
  }
  .afterStart{
    justify-content: space-between;
  }
  .id_add_data_block{
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: space-around;
    height: 200px;
  }

  @media only screen and (max-width: 1024px) {
    .info_card{
      margin-bottom: 20px;
      margin-top: 0;
    }
  }

</style>