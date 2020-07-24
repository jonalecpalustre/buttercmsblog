

<template>
  <div id="app">
    <figure>
      <img :src="page.fields.hero_image">
    </figure>
    <h1>{{ page.fields.headline }}</h1>
    <button>{{ page.fields.call_to_action }}</button>

    <h3>Customers Love Us!</h3>
    <!-- Loop over customer logos -->
    <img v-for="logo in page.fields.customer_logos" :src="logo.logo_image">
  </div>
</template>


<script>
  import { butter } from '@/buttercms'
  export default {
    name: 'sample-page',
    data() {
      return {
        page: {
          fields: {}
        }
      }
    },
    methods: {
      getPage() {
        butter.page.retrieve('*', 'sample-page')
          .then((res) => {
            console.log(res.data.data)
            this.page = res.data.data
          }).catch((res) => {
            console.log(res)
          })
      }
    },
    created() {
      this.getPage()
    }
  }
</script>
