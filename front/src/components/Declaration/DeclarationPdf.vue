<template>
  <div v-show="false" id="id_declaration_pdf_body">
    <declaration-body :inputs="inputs"/>
  </div>
</template>

<script>
import DeclarationBody from "./DeclarationBody.vue";
export default {
  name: "DeclarationPdf",
  components: {DeclarationBody},
  props: ['inputs'],
}
</script>

<style scoped>
  div:deep(.book){
    font: 11pt "Times New Roman";
  }
  div:deep(hr){
    margin: 5px 0;
  }
  div:deep(td){
    height: 18px;
  }
  div:deep(.page){
    width: 210mm;
    padding: 8mm 10mm 0 25mm;
    background: white;
  }
</style>