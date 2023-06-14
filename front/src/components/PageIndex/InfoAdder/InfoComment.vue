<template>
  <div id="comment-text-block">
    <textarea
        :value="commentos"
        ref="textField"
        :maxlength="maxl"
        :placeholder="placeholder"
        @input="evt => commentos = evt.target.value"
    />
    <div id="id-under-text">
      <span
          v-if="errorTxt"
          id="id-comment-error"
      >
        {{errorTxt}}
      </span>
      <span v-else>
        Осталось символов: {{maxl - commentos.length}}
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfoComment",
  props: {
    isComplaint: { type: Boolean, default: false },
    finalObject: { type: Object, default: () => ({}) },
  },
  data() {
    return {
      maxl: 256,
      commentos: '',
      errorTxt: '',
    }
  },
  mounted() {
    this.$refs.textField.focus();
  },
  computed: {
    placeholder() {
      if (this.isComplaint) {
        return 'Введите текст';
      }
      return 'Напишите здесь комментарий или нажмите Далее чтобы пропустить этот шаг';
    },
  },
  methods: {
    getResult() {
      return this.commentos;
    },
    isValid() {
      if(!this.commentos.trim().length) {
        this.errorTxt = 'Напишите текст жалобы';
        this.$refs.textField.focus();
        return false;
      }
      this.errorTxt = '';
      return true;
    },
  },
}
</script>

<style scoped>
  #comment-text-block{
    display: flex;
    flex: 1;
    flex-direction: column;
  }
  textarea{
    display: flex;
    flex: 1;
    box-sizing: border-box;
    font-size: 18px;
    resize: none;
  }
  #id-under-text{
    text-align: right;
    font-size: 14px;
    margin-bottom: 15px;
  }
  #id-comment-error{
    color: #ff8f66;
  }
</style>