/** @module module */

/** Klasa reprezentująca operację. */
class Operation {
  /**
   * Stwórz operację.
   * @param {number} x - Wartość pierwszego składnika.
   * @param {number} y - Wartość drugiego składnika.
   */
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Zsumuj podane w definicji klasy wartości x i y.
   * @return {number} - Suma wartości x i y.
   */
  sum() {
    return this.x + this.y;
  }
}

export {Operation} 