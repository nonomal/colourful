package storage

import (
	"testing"
)

func TestSign(t *testing.T) {
	sign, err := sign("testsign")
	if err != nil {
		t.Error(err)
	}
	t.Log(sign)

}
