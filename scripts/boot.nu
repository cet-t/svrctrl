def main [] {
  let proc_count = (netstat -ano | find ":25565" | length);
  let is_running = $proc_count > 0;
  $is_running
}
