<template>
  <div :class="is_grey ? 'loader_grey' : 'loader'">Loading...</div>
</template>

<script>
export default {
  name: "Spinner",
  props:['is_grey',],
}
</script>

<style scoped>
.loader {
  margin: 73px auto 73px auto;
  justify-content: space-around;
  font-size: 16px;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  position: relative;
  text-indent: -9999em;
  -webkit-animation: load5 1.1s infinite ease;
  animation: load5 1.1s infinite ease;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
}
@-webkit-keyframes load5 {
  0%,
  100% {
    box-shadow: 0em -2.6em 0em 0em #ffffff, 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.5), -1.8em -1.8em 0 0em rgba(255,255,255, 0.7);
  }
  12.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.7), 1.8em -1.8em 0 0em #ffffff, 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.5);
  }
  25% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.5), 1.8em -1.8em 0 0em rgba(255,255,255, 0.7), 2.5em 0em 0 0em #ffffff, 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  37.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.5), 2.5em 0em 0 0em rgba(255,255,255, 0.7), 1.75em 1.75em 0 0em #ffffff, 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  50% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.5), 1.75em 1.75em 0 0em rgba(255,255,255, 0.7), 0em 2.5em 0 0em #ffffff, -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  62.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.5), 0em 2.5em 0 0em rgba(255,255,255, 0.7), -1.8em 1.8em 0 0em #ffffff, -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  75% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.5), -1.8em 1.8em 0 0em rgba(255,255,255, 0.7), -2.6em 0em 0 0em #ffffff, -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  87.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.5), -2.6em 0em 0 0em rgba(255,255,255, 0.7), -1.8em -1.8em 0 0em #ffffff;
  }
}
@keyframes load5 {
  0%,
  100% {
    box-shadow: 0em -2.6em 0em 0em #ffffff, 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.5), -1.8em -1.8em 0 0em rgba(255,255,255, 0.7);
  }
  12.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.7), 1.8em -1.8em 0 0em #ffffff, 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.5);
  }
  25% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.5), 1.8em -1.8em 0 0em rgba(255,255,255, 0.7), 2.5em 0em 0 0em #ffffff, 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  37.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.5), 2.5em 0em 0 0em rgba(255,255,255, 0.7), 1.75em 1.75em 0 0em #ffffff, 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  50% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.5), 1.75em 1.75em 0 0em rgba(255,255,255, 0.7), 0em 2.5em 0 0em #ffffff, -1.8em 1.8em 0 0em rgba(255,255,255, 0.2), -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  62.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.5), 0em 2.5em 0 0em rgba(255,255,255, 0.7), -1.8em 1.8em 0 0em #ffffff, -2.6em 0em 0 0em rgba(255,255,255, 0.2), -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  75% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.5), -1.8em 1.8em 0 0em rgba(255,255,255, 0.7), -2.6em 0em 0 0em #ffffff, -1.8em -1.8em 0 0em rgba(255,255,255, 0.2);
  }
  87.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255,255,255, 0.2), 1.8em -1.8em 0 0em rgba(255,255,255, 0.2), 2.5em 0em 0 0em rgba(255,255,255, 0.2), 1.75em 1.75em 0 0em rgba(255,255,255, 0.2), 0em 2.5em 0 0em rgba(255,255,255, 0.2), -1.8em 1.8em 0 0em rgba(255,255,255, 0.5), -2.6em 0em 0 0em rgba(255,255,255, 0.7), -1.8em -1.8em 0 0em #ffffff;
  }
}


.loader_grey {
  margin: 73px auto 73px auto;
  justify-content: space-around;
  font-size: 16px;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  position: relative;
  text-indent: -9999em;
  -webkit-animation: load6 1.1s infinite ease;
  animation: load6 1.1s infinite ease;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
}
@-webkit-keyframes load6 {
  0%,
  100% {
    box-shadow: 0em -2.6em 0em 0em #bbb9b9, 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.5), -1.8em -1.8em 0 0em rgba(187,185,185, 0.7);
  }
  12.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.7), 1.8em -1.8em 0 0em #bbb9b9, 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.5);
  }
  25% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.5), 1.8em -1.8em 0 0em rgba(187,185,185, 0.7), 2.5em 0em 0 0em #bbb9b9, 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  37.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.5), 2.5em 0em 0 0em rgba(187,185,185, 0.7), 1.75em 1.75em 0 0em #bbb9b9, 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  50% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.5), 1.75em 1.75em 0 0em rgba(187,185,185, 0.7), 0em 2.5em 0 0em #bbb9b9, -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  62.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.5), 0em 2.5em 0 0em rgba(187,185,185, 0.7), -1.8em 1.8em 0 0em #bbb9b9, -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  75% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.5), -1.8em 1.8em 0 0em rgba(187,185,185, 0.7), -2.6em 0em 0 0em #bbb9b9, -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  87.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.5), -2.6em 0em 0 0em rgba(187,185,185, 0.7), -1.8em -1.8em 0 0em #bbb9b9;
  }
}
@keyframes load6 {
  0%,
  100% {
    box-shadow: 0em -2.6em 0em 0em #bbb9b9, 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.5), -1.8em -1.8em 0 0em rgba(187,185,185, 0.7);
  }
  12.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.7), 1.8em -1.8em 0 0em #bbb9b9, 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.5);
  }
  25% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.5), 1.8em -1.8em 0 0em rgba(187,185,185, 0.7), 2.5em 0em 0 0em #bbb9b9, 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  37.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.5), 2.5em 0em 0 0em rgba(187,185,185, 0.7), 1.75em 1.75em 0 0em #bbb9b9, 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  50% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.5), 1.75em 1.75em 0 0em rgba(187,185,185, 0.7), 0em 2.5em 0 0em #bbb9b9, -1.8em 1.8em 0 0em rgba(187,185,185, 0.2), -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  62.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.5), 0em 2.5em 0 0em rgba(187,185,185, 0.7), -1.8em 1.8em 0 0em #bbb9b9, -2.6em 0em 0 0em rgba(187,185,185, 0.2), -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  75% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.5), -1.8em 1.8em 0 0em rgba(187,185,185, 0.7), -2.6em 0em 0 0em #bbb9b9, -1.8em -1.8em 0 0em rgba(187,185,185, 0.2);
  }
  87.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(187,185,185, 0.2), 1.8em -1.8em 0 0em rgba(187,185,185, 0.2), 2.5em 0em 0 0em rgba(187,185,185, 0.2), 1.75em 1.75em 0 0em rgba(187,185,185, 0.2), 0em 2.5em 0 0em rgba(187,185,185, 0.2), -1.8em 1.8em 0 0em rgba(187,185,185, 0.5), -2.6em 0em 0 0em rgba(187,185,185, 0.7), -1.8em -1.8em 0 0em #bbb9b9;
  }
}

</style>