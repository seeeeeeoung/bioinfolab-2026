LEN=${#SEQ}
GC=$(echo "$SEQ" | grep -o "[GC]" | wc -l)
RATIO=$(echo "scale=4; $GC / $LEN" | bc)
NCOUNT=$(echo "$SEQ" | grep -o "N" | wc -l)

if [ "$LEN" -ge 500 ] && [ "$LEN" -le 3000 ]
then
  if [ "$(echo "$RATIO >= 0.4" | bc)" -eq 1 ] && [ "$(echo "$RATIO <= 0.6" | bc)" -eq 1 ]
  then
    if ! echo "$NAME" | grep -q "partial"
    then
      if [ "$NCOUNT" -lt 5 ]
      then
        echo "$NAME"
      fi
    fi
  fi
fi