<template>
  <div class="block_big" id="id_big_donate">
    <div class="block_inner" id="id_donate">

      <div id="id_donate_head">
        <h6>ПОДДЕРЖИТЕ САЙТ</h6>
        <div class="under_h6">
            КППшка - это некоммерческий проект и абсолютно бесплатный.
          Единственный способ существования и развитие сайта - это помощь земляков и всех людей которым сайт приносит пользу.
          <br>
          <br>
          В будущем планируется добавление еще нескольких полезных разделов.
          <br>
          <br>
          Если у вас нет возможности финансово поддержать проект, вы можете рассказать о нем в соц. сетях, и поделиться ссылкой.
          <br>
          <br>
          Огромная благодарность всем кто оказал и оказывает поддержку!
        </div>
      </div>
      <div id="block_donate">
        <div class="sub_block_wrp">
          <div class="sub_block">
            <header class="sub_header">Поделитесь ссылкой на сайт:</header>
            <div class="ya-share2"
                 data-curtain
                 data-size="l"
                 data-shape="round"
                 data-services="vkontakte,odnoklassniki,moimir,telegram,viber,whatsapp,skype,facebook"
            />
          </div>
          <div class="sub_block">
            <header class="sub_header">Отправьте благодарочку:</header>
            <p>СБЕР: 4817 7602 6759 0580</p>
            <p>- или -</p>
            <p>Ю money:</p>
            <iframe src="https://yoomoney.ru/quickpay/shop-widget?writer=seller&targets=%D0%9D%D0%B0%20%D1%80%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5%20%D0%9A%D0%9F%D0%9F%D1%88%D0%BA%D0%B8&targets-hint=&default-sum=100&button-text=12&payment-type-choice=on&hint=&successURL=&quickpay=shop&account=4100183011918" width="300" height="222" frameborder="0" allowtransparency="true" scrolling="no"></iframe>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlockDonates"
}
</script>

<style scoped>
.sub_header{
  margin-bottom: 25px;
  color: #347ae3;
  font-size: 1.2em;
  font-weight: 400;
}
.sub_block_wrp{
  min-height: 450px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0 10px;
}
.sub_block:last-of-type {
  margin-top: 40px;
}
.ya-share2{
  text-align: center;
}
h6{
  font-size: 2.5em;
  margin-top: 20px;
  margin-bottom: 0;
  font-weight: 200;
  color: #e37534;
}
.under_h6{
  font-weight: 200;
  font-size: 1.2em;
  margin-top: 15px;
  margin-bottom: 15px;
}
#id_donate{
  display: flex;
  flex-wrap: wrap;
}
#id_donate_head{
  flex: 1;
  max-width: 720px;
}
#id_big_donate{
  background-color: papayawhip;
  padding: 50px 0;
}

#block_donate{
  padding: 40px 0;
  display: flex;
  justify-content: space-around;
  flex: 0 1 720px;
  flex-wrap: wrap;
}
@media only screen and (max-width: 420px) {
  #id_donate_head {
    /*text-align: center;*/
    padding: 0 20px;
  }
  h6{
    text-align: center;
    font-size: 2.3em;
  }
  .sub_block {
    text-align: center;
  }
  .sub_block:last-of-type {
    margin-top: 70px;
  }
}

</style>