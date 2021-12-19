import axios from 'axios'

export const getPaintings = ({ commit }, url) => {
  if (url != false && url != null) {
    axios
      .get(url)
      .then((response) => {
        commit('receivePaginatedPaintings', response.data)
      })
      .catch((e) => console.error(e))
  }
}
