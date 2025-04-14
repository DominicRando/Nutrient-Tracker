import { LitElement, html, css } from 'https://unpkg.com/lit@3.1.0?module';

class SearchDropdown extends LitElement {
  static styles = css`
    .container {
    display: inline-block; /* keep dropdown size in line with input */
    position: relative;
    width: 400px;
    font-family: sans-serif;
  }

  input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border-radius: 15px;
    border: 2px solid black;
    box-sizing: border-box;
  }

  .dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background: white;
  border: 1px solid #ccc;
  max-height: 200px;
  overflow-y: auto;
  box-sizing: border-box;
  z-index: 10;
}

  .item {
    padding: 10px;
    text-align: center;
    cursor: pointer;
    border-bottom: 1px solid #f1f1f1;
  }

  .item:last-child {
    border-bottom: none;
  }

  .item:hover {
    background-color: #f0f0f0;
  }
  `;

  static properties = {
    inputValue: { type: String },
    results: { type: Array }
  };

  constructor() {
    super(); // Have to include this: 
    this.inputValue = '';
    this.results = [];
    this._latestRequest = 0;
  }

  async handleInput(event) {
    this.inputValue = event.target.value.trim();
    const currentRequest = ++this._latestRequest;
  
    if (!this.inputValue) {
      this.results = [];
      return;
    }
  
    try {
      const response = await fetch(`http://localhost:8080/api/products?name=${encodeURIComponent(this.inputValue)}`);
      const data = await response.json();
  
      // If this request is outdated, ignore it
      if (currentRequest !== this._latestRequest) return;
  
      this.results = Array.isArray(data)
        ? data.map(p => p.product_name).sort((a, b) => a.length - b.length)
        : [data.product_name];
    } catch (err) {
      if (currentRequest === this._latestRequest) {
        console.error('API call failed:', err);
        this.results = [];
      }
    }
  }
  

  handleSelect(option) {
    this.inputValue = option;
    this.results = [];
  }

  render() {
    return html`
      <div class="container">
        <input
          type="text"
          .value=${this.inputValue}
          @input=${this.handleInput}
          placeholder="Search..."
        />
        ${this.results.length > 0
          ? html`
              <div class="dropdown">
                ${this.results.map(
                  item => html`
                    <div class="item" @click=${() => this.handleSelect(item)}>
                      ${item}
                    </div>
                  `
                )}
              </div>
            `
          : ''}
      </div>
    `;
  }
}

customElements.define('search-dropdown', SearchDropdown);
