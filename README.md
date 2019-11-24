# Ansible Collection Sample

## Install

    $ git clone https://github.com/m-takahashi-if/ansible-collection-sample
    $ ansible-galaxy collection build ansible-collection-sample
    $ ansible-galaxy collection install ac_sample-calc-1.0.0.tar.gz


## Calc Server

    ansible-playbook --> playbook --> role/module --(HTTP)--> Calc Server

See https://github.com/m-takahashi-if/ansible-collection-demo .

## Using sample module

### add 10

    - name: clear and add 10
      ac_sample.calc.publish_request:
        value: 10

### Clear result

    - name: clear and add 10
      ac_sample.calc.publish_request:
        command: clear

### Clear result and add 10

    - name: clear and add 10
      ac_sample.calc.publish_request:
        command: clear
        value: 10

## Using sample role

### Add 10

    roles:
      - role: ac_sample.calc.add
        vars:
          value: 10

### Clear result

    roles:
      - role: ac_sample.calc.clear
