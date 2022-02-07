<?php

namespace App\Jobs\Middleware;

use Illuminate\Support\Facades\Redis;

class RateLimited
{
  public function handle(mixed $job, callable $next)
  {
    Redis::throttle('key')
      ->block(1)
      ->allow(1)
      ->every(1)
      ->then(function () use ($job, $next) {
        $next($job);
      }, function () use ($job) {
        $job->release(5);
      });
  }
}
