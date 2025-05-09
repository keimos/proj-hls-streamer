module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8080/api/:path*', // Proxy to Backend
      },
      {
        source: '/:path*',
        destination: 'http://localhost:8000/streams/:path*', // Proxy to Frontend
      },
    ];
},
};