export default function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white px-8 py-10 font-sans">
      <h1 className="text-4xl font-bold mb-8">DealLab: M&A Deal Screener</h1>
      
      <div className="flex flex-col sm:flex-row gap-4 mb-10">
        <input
          type="text"
          placeholder="Enter Company Name or Ticker (e.g. Google or GOOGL)"
          className="flex-1 p-4 rounded-xl bg-gray-800 placeholder-gray-400 border border-gray-700"
        />
        <button className="px-6 py-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white">
          Run Analysis
        </button>
      </div>

      {/* Placeholder for results */}
      <div id="results" className="space-y-6">
        <div className="p-6 bg-gray-800 rounded-xl shadow">🔍 Company Info will show here</div>
        <div className="p-6 bg-gray-800 rounded-xl shadow">📊 Strategy Suggestions</div>
        <div className="p-6 bg-gray-800 rounded-xl shadow">📈 Forecast Charts</div>
        <div className="p-6 bg-gray-800 rounded-xl shadow">🧠 Signals Summary</div>
      </div>
    </div>
  );
}
