/* ---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *-------------------------------------------------------------------------------------------- */
import * as path from 'path';
import { CodeModelAz } from '../../CodeModelAz';
import { TemplateBase } from '../TemplateBase';
import { PathConstants } from '../../../utils/models';

export class CliTestInit extends TemplateBase {
    constructor(model: CodeModelAz) {
        super(model);
        if (this.model.IsCliCore) {
            this.relativePath = path.join(PathConstants.testFolder, PathConstants.initFile);
        } else {
            this.relativePath = path.join(
                model.AzextFolder,
                PathConstants.testFolder,
                PathConstants.initFile,
            );
        }
    }

    public fullGeneration(): string[] {
        return this.GenerateAzureCliTestInit(this.model);
    }

    public incrementalGeneration(base: string): string[] {
        return this.fullGeneration();
    }

    private GenerateAzureCliTestInit(model: CodeModelAz): string[] {
        const output: string[] = [];

        output.push('# coding=utf-8');
        output.push('# --------------------------------------------------------------------------');
        output.push('# Copyright (c) Microsoft Corporation. All rights reserved.');
        output.push('# Licensed under the MIT License. See License.txt in the project root for');
        output.push('# license information.');
        output.push('#');
        output.push('# Code generated by Microsoft (R) AutoRest Code Generator.');
        output.push('# Changes may cause incorrect behavior and will be lost if the code is');
        output.push('# regenerated.');
        output.push('# --------------------------------------------------------------------------');
        output.push('import inspect');
        output.push('import logging');
        output.push('import os');
        output.push('import sys');
        output.push('import traceback');
        output.push('import datetime as dt');
        output.push('');
        output.push('from azure.core.exceptions import AzureError');
        output.push(
            'from azure.cli.testsdk.exceptions import CliTestError, CliExecutionError, JMESPathCheckAssertionError',
        );
        output.push('');
        output.push('');
        output.push("logger = logging.getLogger('azure.cli.testsdk')");
        output.push('logger.addHandler(logging.StreamHandler())');
        output.push("__path__ = __import__('pkgutil').extend_path(__path__, __name__)");
        output.push('exceptions = []');
        output.push('test_map = dict()');
        output.push('SUCCESSED = "successed"');
        output.push('FAILED = "failed"');
        output.push('');
        output.push('');
        output.push('def try_manual(func):');
        output.push('    def import_manual_function(origin_func):');
        output.push('        from importlib import import_module');
        output.push('        decorated_path = inspect.getfile(origin_func).lower()');
        output.push('        module_path = __path__[0].lower()');
        output.push('        if not decorated_path.startswith(module_path):');
        output.push('            raise Exception("Decorator can only be used in submodules!")');
        output.push('        manual_path = os.path.join(');
        output.push('            decorated_path[module_path.rfind(os.path.sep) + 1:])');
        output.push('        manual_file_path, manual_file_name = os.path.split(manual_path)');
        output.push('        module_name, _ = os.path.splitext(manual_file_name)');
        output.push('        manual_module = "..manual." + \\');
        output.push('            ".".join(manual_file_path.split(os.path.sep) + [module_name, ])');
        output.push(
            '        return getattr(import_module(manual_module, package=__name__), origin_func.__name__)',
        );
        output.push('');
        output.push('    def get_func_to_call():');
        output.push('        func_to_call = func');
        output.push('        try:');
        output.push('            func_to_call = import_manual_function(func)');
        output.push('            logger.info("Found manual override for %s(...)", func.__name__)');
        output.push('        except (ImportError, AttributeError):');
        output.push('            pass');
        output.push('        return func_to_call');
        output.push('');
        output.push('    def wrapper(*args, **kwargs):');
        output.push('        func_to_call = get_func_to_call()');
        output.push('        logger.info("running %s()...", func.__name__)');
        output.push('        try:');
        output.push('            test_map[func.__name__] = dict()');
        output.push('            test_map[func.__name__]["result"] = SUCCESSED');
        output.push('            test_map[func.__name__]["error_message"] = ""');
        output.push('            test_map[func.__name__]["error_stack"] = ""');
        output.push('            test_map[func.__name__]["error_normalized"] = ""');
        output.push('            test_map[func.__name__]["start_dt"] = dt.datetime.utcnow()');
        output.push('            ret = func_to_call(*args, **kwargs)');
        output.push(
            '        except (AssertionError, AzureError, CliTestError, CliExecutionError, SystemExit,',
        );
        output.push('                JMESPathCheckAssertionError) as e:');
        output.push('            use_exception_cache = os.getenv("TEST_EXCEPTION_CACHE")');
        output.push(
            '            if use_exception_cache is None or use_exception_cache.lower() != "true":',
        );
        output.push('                raise');
        output.push('            test_map[func.__name__]["end_dt"] = dt.datetime.utcnow()');
        output.push('            test_map[func.__name__]["result"] = FAILED');
        output.push(
            '            test_map[func.__name__]["error_message"] = str(e).replace("\\r\\n", " ").replace("\\n", " ")[:500]',
        );
        output.push(
            '            test_map[func.__name__]["error_stack"] = traceback.format_exc().replace(',
        );
        output.push('                "\\r\\n", " ").replace("\\n", " ")[:500]');
        output.push('            logger.info("--------------------------------------")');
        output.push('            logger.info("step exception: %s", e)');
        output.push('            logger.error("--------------------------------------")');
        output.push('            logger.error("step exception in %s: %s", func.__name__, e)');
        output.push('            logger.info(traceback.format_exc())');
        output.push('            exceptions.append((func.__name__, sys.exc_info()))');
        output.push('        else:');
        output.push('            test_map[func.__name__]["end_dt"] = dt.datetime.utcnow()');
        output.push('            return ret');
        output.push('');
        output.push('    if inspect.isclass(func):');
        output.push('        return get_func_to_call()');
        output.push('    return wrapper');
        output.push('');
        output.push('');
        output.push('def calc_coverage(filename):');
        output.push('    filename = filename.split(".")[0]');
        output.push('    coverage_name = filename + "_coverage.md"');
        output.push('    with open(coverage_name, "w") as f:');
        output.push(
            '        f.write("|Scenario|Result|ErrorMessage|ErrorStack|ErrorNormalized|StartDt|EndDt|\\n")',
        );
        output.push('        total = len(test_map)');
        output.push('        covered = 0');
        output.push('        for k, v in test_map.items():');
        output.push('            if not k.startswith("step_"):');
        output.push('                total -= 1');
        output.push('                continue');
        output.push('            if v["result"] == SUCCESSED:');
        output.push('                covered += 1');
        output.push(
            '            f.write("|{step_name}|{result}|{error_message}|{error_stack}|{error_normalized}|{start_dt}|"',
        );
        output.push('                    "{end_dt}|\\n".format(step_name=k, **v))');
        output.push('        f.write("Coverage: {}/{}\\n".format(covered, total))');
        output.push('    print("Create coverage\\n", file=sys.stderr)');
        output.push('');
        output.push('');
        output.push('def raise_if():');
        output.push('    if exceptions:');
        output.push('        if len(exceptions) <= 1:');
        output.push('            raise exceptions[0][1][1]');
        output.push(
            '        message = "{}\\nFollowed with exceptions in other steps:\\n".format(str(exceptions[0][1][1]))',
        );
        output.push(
            '        message += "\\n".join(["{}: {}".format(h[0], h[1][1]) for h in exceptions[1:]])',
        );
        output.push(
            '        raise exceptions[0][1][0](message).with_traceback(exceptions[0][1][2])',
        );
        output.push('');

        return output;
    }

    public GetRenderData(model: CodeModelAz): string[] {
        const output: string[] = [];
        return output;
    }
}
