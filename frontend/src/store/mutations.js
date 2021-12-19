export default {
  receivePaginatedPaintings(state, paintings) {
    const { results, count, next, previous } = paintings

    state.paintings.data = results
    state.paintings.count = count
    state.paintings.paginator.next = next
    state.paintings.paginator.previous = previous
  },
}
