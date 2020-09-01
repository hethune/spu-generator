<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>SPUs</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Generate SPUs</button>
        <br><br>
        Total SPU Genrated: {{total_spus}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      total_spus: 0,
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
