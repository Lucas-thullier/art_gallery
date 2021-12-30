export default {
  receivePaginatedPaintings(state, paintings) {
    const { results, count, next, previous } = paintings

    state.paintings.data = results
    state.paintings.count = count
    state.paintings.paginator.next = next
    state.paintings.paginator.previous = previous
  },

  receivePaginatedCreators(state, creators) {
    const { results, count, next, previous } = creators

    state.creators.data = results
    state.creators.count = count
    state.creators.paginator.next = next
    state.creators.paginator.previous = previous
  },
}
