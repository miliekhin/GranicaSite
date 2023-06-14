<template>
  <div>
    Данные снова можно будет отправить примерно через
    <br>
    <br>
    {{timeText}}
  </div>
</template>

<script>
export default {
  name: "InfoWait",
  props: {
    finalObject: { type: Object, default: () => ({}) },
  },
  data() {
    return {
      ok: true,
    }
  },
  computed: {
    timeText() {
      const sentTime = localStorage.getItem('sent')
      const sent = new Date(sentTime)
      const now = new Date()
      const unblockedAfterMs = this.SEND_INFO_PERIOD_LIMIT - (now - sent);
      if(unblockedAfterMs <= 0) {
        return '0';
      }
      const mins = Math.floor(unblockedAfterMs / 1000 / 60) + 1
      const minEnd = (m) => {
        if (m === 1)
          return 'у';
        if (m < 5)
          return  'ы';
        return '';
      }
      const txt = `${mins} минут${minEnd(mins)}`;
      return txt;
    },
  }
}
</script>

<style scoped>
  div{
    text-align: center;
    font-size: 18px;
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: center;
    line-height: 1.5em;
  }
</style>